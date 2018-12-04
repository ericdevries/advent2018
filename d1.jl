pwd()
println("hello")
println("hello")

function r(filename)
    numbers = Int64[]

    open("d1input.txt") do file
        for line in eachline(file)
            num = parse(Int, line)
            push!(numbers, num)
        end
    end 

    numbers
end

function r2()
    numbers = r("d1input")
    occured = Set{Int64}()
    current = 0

    while true
        for item in numbers
            new_value = current + item
            
            if new_value in occured 
                return new_value
            end
            current = new_value
            push!(occured, new_value)
        end
        println("loop")
    end
end

first_value = r2()
println("first value: $(first_value)")
