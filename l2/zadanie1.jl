using JuMP
using GLPK

function readFile()
    dir = "/Volumes/SamsungT5/aod/l2/model.txt"
    open(dir) do f
        numberAirportsAndCompaniesResorces =parse.(Int, split(readline(f), ";"))
        aname = ["A$i" for i in 1:numberAirportsAndCompaniesResorces[1]]
        cname = ["C$i" for i in 1:numberAirportsAndCompaniesResorces[2]]
        append!(aname , ["BIN"])

        boundCompaniesResorces = parse.(Int, split(readline(f), ";"))
        boundAirportsResorces = parse.(Int, split(readline(f), ";"))

        diff = sum(boundCompaniesResorces) - sum(boundAirportsResorces)
        append!(boundAirportsResorces, diff)

        shoping = zeros(Int, length(aname), length(cname))

        for i in 1:length(aname)-1
            line = parse.(Int, split(readline(f), ";"))    
            for l in 1:length(line)
                shoping[i, l] = line[l]
            end
        end

        d = Dict((aname[i], cname[j]) => shoping[i, j] for i in 1:length(aname), j in 1:length(cname))

        return aname, cname, boundCompaniesResorces, boundAirportsResorces, d
    end
end



function run(airportsname, companiesname, boundCompanies, boundAirports, shoppingDict)
    model = Model(GLPK.Optimizer)

    @variable(model, x[airportsname, companiesname] >= 0)
    
    @objective(model, Min,
        sum(shoppingDict[i, j] * x[i, j] for i in airportsname, j in companiesname)
    )

    for (i, b) in zip(airportsname, boundAirports)
        @constraint(model, sum(x[i, j] for j in companiesname) == b)
    end

    for (i, b) in zip(companiesname, boundCompanies)
        @constraint(model, sum(x[j, i] for j in airportsname) == b)
    end

    optimize!(model)
    # print(model)
    # latex_formulation(model)
    print(value.(x))
end

f = readFile()
run(f[1], f[2], f[3], f[4], f[5])
