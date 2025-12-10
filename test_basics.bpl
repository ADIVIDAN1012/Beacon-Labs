spec main:
    show "--- Testing Basics ---"
    show "1. Variables & Types"
    firm pi = 3.14
    count = 0
    firm name = "Beacon"
    firm is_active = On
    
    show "Pi: |pi|"
    show "Count: |count|"
    show "Name: |name|"
    show "Active: |is_active|"
    
    show "2. Math Operations"
    firm val1 = 10
    firm val2 = 5
    show "10 + 5 = |val1 + val2|"
    show "10 - 5 = |val1 - val2|"
    show "10 * 5 = |val1 * val2|"
    show "10 / 5 = |val1 / val2|"
    
    show "3. Control Flow (when/otherwise)"
    when count == 0:
        show "Count is zero (Correct)"
    otherwise when count > 0:
        show "Count is positive (Incorrect)"
    otherwise:
        show "Count is negative (Incorrect)"
    done
    
    show "4. Loops (until)"
    i = 0
    until i >= 3:
        show "Loop i: |i|"
        i = i + 1
    done
    
    show "5. Functions"
    firm res = add(5, 7)
    show "5 + 7 = |res|"
    
    show "--- Basics Verification Complete ---"
done

spec add with v1, v2:
    forward v1 + v2
done

main()
