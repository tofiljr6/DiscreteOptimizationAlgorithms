# import Pkg
# Pkg.add("JuMP")
# Pkg.add("GLPK")

using JuMP
using GLPK
model = Model(GLPK.Optimizer)
@variable(model, 0 <= x <= 200)
@variable(model, 0 <= y <= 300)
@objective(model, Max, x + 6y)
@constraint(model, c1, x + y <= 400)
print(model)
optimize!(model)
@show termination_status(model)
@show primal_status(model)
@show dual_status(model)
@show objective_value(model)
@show value(x)
@show value(y)
@show shadow_price(c1)


println("INTERPRETACJA: ")
println("Ilość do wyprodukowania czekolady mlecznej ", value(x))
println("Ilość do wyprodukowania czekolady luksusowej ", value(y))