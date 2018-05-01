def get_response(prompt, options):
    """Print a prompt and get user response, returning only if valid.

    prompt  the prompt string
    options  iterable containing legal response characters

    Returns the legal response character.
    """

    # ensure legal options are lowercase
    lower_options = [ch.lower() for ch in options]

    # prompt user until legal response
    while True:
        try:
            response = input(prompt)[0].lower()
        except IndexError:
            response = None
        if response in lower_options:
            return response

yay = 'Yay!'

collectionMethod = get_response("Please Press 'P' For Pickup or Press 'D' For Delivery",
                                ('p', 'd'))
if collectionMethod == 'd':
    deliveryAddress = input("Please enter the Delivery address e.g. (123 Hamilton Rd, Hillcrest)")
else:
    print(yay)

orderName = get_response("Please Enter The Order Name", ('1', '2', '3', '4', '5'))

pizzaNumber = get_response("Please Enter The Number Of Pizzas Being Ordered (Maximum of 5)",
                           ('1', '2', '3', '4', '5'))
