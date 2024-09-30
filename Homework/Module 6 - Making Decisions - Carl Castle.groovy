WHILE true
    OUTPUT "Enter -1 if you would like to exit"
    INPUT userWish
    IF userWish == -1
        BREAK
    ENDIF

    OUTPUT "Enter area code:"
    INPUT areaCode

    OUTPUT "Enter phone number:"
    INPUT phoneNumber
    IF NumsIn(phoneNumber) == 10 // in case the user still input their area code in the phone number
        RemoveFirstThreeFrom(phoneNumber)
    ENDIF
    
    OUTPUT "Enter total number of texts sent: " // I'm sure no customer would ever lie about this, right?
    input totalTexts

    VAR bill = 0

    IF totalTexts <= 100
        bill = 5
    ELSE IF totalTexts <= 300
        bill = 5 + ((totalTexts - 100) * .03)
    ELSE
        bill = 5 + (200 * .03) + ((totalTexts - 300) * .02)
    ENDIF

    billTax = bill * 1.14

    // I'm aware string concatenation wouldn't work here, as there values are integers, but shhhhh
    // there are functions defined for the output, each one is defined by which scenario you'd like to run

    DEFINE FUNCTION output(areaCode, phoneNumber, totalTexts, bill, billTax)
        OUTPUT "Area Code: " + areaCode
        OUTPUT "Phone Number: " + phoneNumber
        OUTPUT "Texts Sent: " + totalTexts
        OUTPUT "Pre-Tax Bill: $" + bill
        OUTPUT "Taxed Bill: $" + billTax
    END FUNCTION

    DEFINE FUNCTION displayAll(areaCode, phoneNumber, totalTexts, bill, billTax)
        output(areaCode, phoneNumber, totalTexts, bill, billTax)
    END FUNCTION

    DEFINE FUNCTION displayLater(areaCode, phoneNumber, totalTexts, bill, billTax)
        ADD EACH VALUE TO ARRAY (areaCode, phoneNumber, totalTexts, bill, billTax, key) formatted as areaCode[0] and so forth, increment 'key' on every entry
        DISPLAY "Would you like to display results? 1 to display, enter to continue collecting data"
        INPUT userWish // secretly not caring about anything other than 0
        IF userWish == 1
            for i in key
                OUTPUT "Area Code: " + areaCode[i]
                OUTPUT "Phone Number: " + phoneNumber[i]
                OUTPUT "Texts Sent: " + totalTexts[i]
                OUTPUT "Pre-Tax Bill: $" + bill[i]
                OUTPUT "Taxed Bill: $" + billTax[i]
            ENDFOR
        ENDIF
    END FUNCTION

    DEFINE FUNCTION displayOverHundred(areaCode, phoneNumber, totalTexts, bill, billTax)
        IF totalTexts > 100
            output(areaCode, phoneNumber, totalTexts, bill, billTax)
        ELSE
            OUTPUT "Nothing to display"
        ENDIF
    END FUNCTION

    DEFINE FUNCTION displayOverTenDollars(areaCode, phoneNumber, totalTexts, bill, billTax)
        IF billTax > 10
            output(areaCode, phoneNumber, totalTexts, bill, billTax)
        ELSE
            OUTPUT "Nothing to display"
        ENDIF
    END FUNCTION

    DEFINE FUNCTION checkArea(areaCode, phoneNumber, totalTexts, bill, billTax)
        OUTPUT "What area code would you like to check for?"
        INPUT areaCheck
        IF areaCode == areaCheck
            displayLater(areaCode, phoneNumber, totalTexts, bill, billTax)
        ELSE
            OUTPUT "Nothing to display"
        ENDIF


// I have no idea why VS Code decided I was writing in Groovy, but here we are