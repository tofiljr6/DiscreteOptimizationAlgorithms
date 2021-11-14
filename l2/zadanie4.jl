using JuMP
using GLPK

function readFile()
    dir = "/Volumes/SamsungT5/aod/l2/company.txt"

    open(dir) do f
        m = parse(Int, readline(f))
        n = parse(Int, readline(f))
        k = parse(Int, readline(f))
        c = parse(Int, readline(f))

        containers = zeros(Int, c, 2)
        for i in 1:c
            line = parse.(Int, split(readline(f), " "))
            containers[i, 1] = line[1]
            containers[i, 2] = line[2]
        end

        return m, n, k, c, containers
    end
end

function getRange(i, j, m, n, k)
    x = zeros(Int, (k * 2 + 1)^2)
    y = zeros(Int, (k * 2 + 1)^2)

    counter = 1
    for l in -k:k
        for o in -k:k
            if !(i + l < 1 || i + l > m || j + o < 1 || j + o > n)
                x[counter] = i + l
                y[counter] = j + o
            else
                x[counter] = i
                y[counter] = j
            end
            counter += 1
        end
    end

    return x, y, (k * 2 + 1)^2
end

function run()
    f = readFile()

    m =          f[1]
    n =          f[2]
    k =          f[3]
    c =          f[4]
    containers = f[5]
    # N = ["n$i" for i in 1:n]
    # M = ["m$i" for i in 1:m]

    isContainer = zeros(Int, n, m)
    for i in 1:c
        isContainer[containers[i, 1], containers[i, 2]] = 1
    end

    ranges = zeros(n, m)
    for i in 1:n
        for j in 1:m
            if isContainer[i, j] != 1
                r = 0
                for l in -k:k
                    for o in -k:k
                        if l != 0 && o != 0
                            try 
                            if isContainer[i + l , j + o] == 1
                                r += 1
                            end
                            catch LoadError end
                        end
                    end
                end
                ranges[i, j] = r
            end
        end
    end

    model = Model(GLPK.Optimizer)
    
    @variable(model, 0 <= x[i=1:n, j=1:m] <= 1, Int)
    @objective(model, Min, sum(x[i, j] for i in 1:n, j in 1:m))
    
    @constraint(model, sum(x[j, i] * ranges[j, i] for i in 1:m, j in 1:n) >= c)

    for i in 1:c
        r = getRange(containers[i, 1], containers[i, 2], n, m, k)
        @constraint(model, sum(x[r[1][j], r[2][j]] for j in 1:r[3]) >= 1)
    end
    
    optimize!(model)
    for i in 1:n
        for j in 1:m
            print(value.(x)[i, j], "   ")
        end
        println("")
    end

    # latex_formulation(model)
end

run()