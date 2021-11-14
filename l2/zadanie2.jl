using JuMP
using GLPK

function readFile()
    dir = "/Volumes/SamsungT5/aod/l2/graph2.txt"

    open(dir) do f
        n = parse.(Int, readline(f))
        cities = ["City $i" for i in 1:n]
        m = parse.(Int, readline(f))

        arcs = zeros(Int, m, 4)

        for i in 1:m
            line = parse.(Int, split(readline(f), " "))
            arcs[i, 1] = line[1]  
            arcs[i, 2] = line[2]
            arcs[i, 3] = line[3] # cost
            arcs[i, 4] = line[4] # time
        end

        s, t = parse.(Int, split(readline(f), " "))

        Otime = parse.(Int, split(readline(f), " "))[1]

        return n, cities, m,  arcs, s, t, Otime
    end
end


function run()
    f = readFile()

    n =      f[1]
    cities = f[2]
    m =      f[3] # number of edges (arcs)
    arcs =   f[4]
    s  =     f[5] # source node
    t =      f[6] # destination node
    time =   f[7] 

    edgeMatrix = zeros(Int, length(cities), length(cities))
    costMatrix = zeros(Int, length(cities), length(cities))
    timeMatrix = zeros(Int, length(cities), length(cities))

    for i in 1:m
        edgeMatrix[arcs[i, 1], arcs[i, 2]] = 1
        costMatrix[arcs[i, 1], arcs[i, 2]] = arcs[i, 3]
        timeMatrix[arcs[i, 1], arcs[i, 2]] = arcs[i, 4]

    end

    edgeExist = Dict(((cities[i], cities[j])) => edgeMatrix[i, j] for i in 1:length(cities), j in 1:length(cities))
    costsDict = Dict(((cities[i], cities[j])) => costMatrix[i, j] for i in 1:length(cities), j in 1:length(cities))
    timesDict = Dict(((cities[i], cities[j])) => timeMatrix[i, j] for i in 1:length(cities), j in 1:length(cities))

    model = Model(GLPK.Optimizer)
    @variable(model, 0 <= x[cities, cities] <= 1, Int)
    @objective(model, Min, sum(costsDict[i, j] * x[i, j] for i in cities, j in cities))

    # balance 
    for i in 1:n
        if i == s
            @constraint(model, sum(edgeExist[cities[i], j] * x[cities[i], j] - edgeExist[j, cities[i]] * x[j, cities[i]] for j in cities) == 1)
        elseif i == t
            @constraint(model, sum(edgeExist[cities[i], j] * x[cities[i], j] - edgeExist[j, cities[i]] * x[j, cities[i]] for j in cities) == -1)
        else
            @constraint(model, sum(edgeExist[cities[i], j] * x[cities[i], j] - edgeExist[j, cities[i]] * x[j, cities[i]] for j in cities) == 0)
        end
    end

    # time bound
    @constraint(model, sum(timesDict[i, j] * x[i, j] for i in cities, j in cities) <= time)

    optimize!(model)

    # latex_formulation(model)
    print(value.(x))
end

readfile = readFile()
run()
# run(readfile[1], readfile[2], readfile[3], readfile[4], readfile[5], readfile[6])