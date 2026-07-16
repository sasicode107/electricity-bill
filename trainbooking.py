def book_train_ticket():
    # User Input
    source_station = input("Enter the source station: ")
    destination_station = input("Enter the destination station: ")
    date_of_travel = input("Enter the date of travel (YYYY-MM-DD): ")
    num_passengers = int(input("Enter the number of passengers: "))

    # User Selection
    selected_train = input("Enter the name of the train you want to book: ")

    # Confirm Booking
    confirm_booking = input(f"Confirm booking for {selected_train}? (yes/no): ")
    if confirm_booking.lower() == "yes":
        # Payment Process
        # Implement the payment process here
        print("Booking confirmed. Payment processed.")

        # Display Confirmation
        print("Booking Details:")
        print(f"Train: {selected_train}")
        print(f"Date of Travel: {date_of_travel}")
        print(f"Passengers: {num_passengers}")
        print("Thank you for booking with us!")
    else:
        print("Booking canceled.")

book_train_ticket()