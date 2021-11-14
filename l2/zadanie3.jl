using JuMP
using GLPK

function readFile()
    dir = "/Volumes/SamsungT5/aod/l2/polizei.txt"

    open(dir) do f
        s = parse(Int, readline(f))
        shifts = ["Shift $i" for i in 1:s]
        d = parse(Int, readline(f))
        districts = ["District $i" for i in 1:d]

        min = zeros(Int, d, s)
        max = zeros(Int, d, s)

        for i in 1:d
            line = parse.(Int, split(readline(f), " "))
            println(line)
            for j in 1:length(line) 
                min[i, j] = line[j]
            end
        end
        readline(f)

        for i in 1:d
            line = parse.(Int, split(readline(f), " "))
            for j in 1:length(line) 
                max[i, j] = line[j]
            end
        end
        readline(f)

        minShifts = parse.(Int, split(readline(f), " "))
        minDistricts = parse.(Int, split(readline(f), " "))

        return s, shifts, d, districts, min, max, minShifts, minDistricts
    end
end

function run()
    f = readFile()

    s =             f[1]
    shifts =        f[2]
    d =             f[3]
    districts =     f[4]
    min =           f[5]
    max =           f[6]
    minShifts =     f[7]
    minDistricts =  f[8]

    minDict = Dict()
    maxDict = Dict()
    for i in 1:s
        for j in 1:d
            minDict[districts[j], shifts[i]] = min[j, i]
            maxDict[districts[j], shifts[i]] = max[j, i]
        end
    end

    minDict = Dict((districts[j], shifts[i]) => min[j, i] for i in 1:s, j in 1:d)
    maxDict = Dict((districts[j], shifts[i]) => max[j, i] for i in 1:s, j in 1:d)
    
    model = Model(GLPK.Optimizer)
    @variable(model, 0 <= x[districts, shifts], Int)

    @objective(model, Min, sum(x[i, j] for i in districts, j in shifts))

    for i in 1:s
        @constraint(model, sum(x[districts[j], shifts[i]] - x[districts[j], shifts[i]] for j in 1:d) == 0)
    end

    for i in districts
        for j in shifts
            @constraint(model, x[i, j] >= minDict[i, j])
            @constraint(model, x[i, j] <= maxDict[i, j])
        end
    end

    for i in 1:s
        @constraint(model, sum(x[j, shifts[i]] for j in districts) >= minShifts[i])
    end

    for i in 1:d
        @constraint(model, sum(x[districts[i], j] for j in shifts) >= minDistricts[i])
    end

    optimize!(model)

    # latex_formulation(model)
    print(value.(x))
end

run()