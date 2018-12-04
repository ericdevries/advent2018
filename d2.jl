function checksum(name) 
    has_two = false
    has_three = false
    
    parts = split(name, "")

    for p in parts 
        if length(filter(s -> s == p, parts)) == 2
            has_two = true
        end 

        if length(filter(s -> s == p, parts)) == 3
            has_three = true  
        end
    end

    has_two, has_three
end

function different_characters(str1, str2) 
    same = Char[]
    diff = 0

    for (a, b) in zip(str1, str2)
        if a == b
            push!(same, a)
        else
            diff += 1
        end
    end
    
    return same, diff
end

function run()
    twos = 0
    threes = 0

    lines = String[]

    open("d2input.txt") do file
        for line in eachline(file)
            a2, a3 = checksum(line)
            
            if a2 
                twos += 1
            end

            if a3
                threes += 1
            end

            push!(lines, line)
        end
    end

    println("twos $(twos), threes $(threes)")
    println("total: $(twos * threes)")
    
    for line in lines 
        for cmp_line in lines
            same, diff = different_characters(cmp_line, line)

            if diff == 1
                println("lines match: \n$(cmp_line) \n$(line)")
                println("$(join(same))")

            end
        end
    end
end

run()
