#------------------------------------------------------ 
# Programmer:   Michael Barreto
# Course:       COSC 1315 Section 10 
# Assignment:   Annual Average Rainfall
#------------------------------------------------------

# Define the main function
def main():
    # Create list for names of the months
    monthList = ["January", "February", "March",
                 "April", "May", "June", "July",
                 "August", "September", "October",
                 "November", "December"]

    # Create list for rain amounts for the months
    monthRain = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

    # Prompt the user for the amount of
    # rain for each month
    num = len(monthList)

    for i in range(num):
        monthRain[i] = float(input("Enter the rainfall for " \
                                    + monthList[i] + ": "))

    # Calculate the total rain
    total = sum(monthRain)

    # Calculate the average rain
    average = total / num

    # Calculate the maximum month rain
    highest = max(monthRain)

    # Get the index of the month with
    # the highest rainfall
    monthHighest = monthRain.index(highest)

    # Calculate the minimum month rain
    lowest = min(monthRain)

    # Get the index of the month with
    # the lowest rainfall
    monthLowest = monthRain.index(lowest)

    # Display results
    print("\nTotal rainfall:", format(total,'.2f') + " in.")
    print("Average rainfall:", format(average, '.2f') + " in.")
    print("Highest rainfall:", monthList[monthHighest],
          "with:", monthRain[monthHighest], "in.")
    print("Lowest rainfall:", monthList[monthLowest],
          "with:", monthRain[monthLowest], "in.")

    # Call the function 'summerStats' to calculate
    # stats for sumer months only
    avgSumRain = summerStats(monthList, monthRain)
    print("Average rain for summer months:",
          format(avgSumRain, '.2f') + " in.")

    # Call the function 'printGoodbye' to
    # Print out closing remarks
    printGoodbye()


# Define the function 'summerStats'. It will
# accept two list parameters, and will calculate
# the total summer rain and average summer rain
# for the summer months only.
def summerStats(monthList, monthRain):
    summerMonths = monthList[5:8]
    summerRain = monthRain[5:8]
    print("\nSummer months:", summerMonths)
    print("Summer rain:", summerRain)

    # Calculate total rain for summer
    # and print it 
    total = sum(summerRain)
    print("Total for summer rain:", format(total, '.2f') + " in.")
    
    # Calculate te average for summer rain
    average = total / len(summerRain)

    # Return the average summer rain
    return average

# Define the function 'printGoodbye'. It will
# display the goodbye message for the program.
def printGoodbye():
    print("\nThis program was written by Michael Barreto.")
    print("End of program")

# Call the main function
main()
    
    
