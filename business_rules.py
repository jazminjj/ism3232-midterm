# Business Rules

NO_DISCOUNT = 0.0
STANDARD_DISCOUNT = 0.05
NONPROFIT_DISCOUNT = 0.12
NONPROFIT_MIN_GUESTS = 100
DISCOUNT_MIN_GUESTS = 25
SERVICE_FEE = 75.0
SERVICE_FEE_LIMIT = 500.0
SIGNOFF_LIMIT = 2500.0
SECOND_CHEF_GUESTS = 80
SECOND_CHEF_TOTAL = 3000.0

# Functions
def calculate_food_cost(guest_price: float, guests: int) -> float:
    """Return the food cost before any discount."""
    return guest_price * guests

def get_event_discount(guests: int, nonprofit: bool = False) -> float:
    """Return the discount rate as a decimal for the guest count."""
    if guests <  DISCOUNT_MIN_GUESTS:
        return NO_DISCOUNT
    if guests >= NONPROFIT_MIN_GUESTS and nonprofit:
        return NONPROFIT_DISCOUNT
    return STANDARD_DISCOUNT

def calculate_event_total(guest_price: float, guests: int, nonprofit: bool = False) -> float:
    """Return the discounted cost plus the service fee"""
    food_cost = calculate_food_cost(guest_price, guests)
    discount = get_event_discount(guests, nonprofit)
    discounted = round(food_cost * (1 - discount), 2)
    if discounted <= SERVICE_FEE_LIMIT:
        discounted += SERVICE_FEE
    return round(discounted, 2)

def needs_signoff(total: float) -> bool:
    """"Return true when the event total requires a manager sign-off"""
    return total > SIGNOFF_LIMIT


def needs_second_chef(guests: int, total: float) -> bool:
    """Return true when event needs a second chef"""
    return guests > SECOND_CHEF_GUESTS or total >= SECOND_CHEF_TOTAL

def total_booked(events: list) -> float:
    """Return the combined total for all booked events"""
    total_booked = 0.0
    for event in events:
        total_booked += calculate_event_total(event["guest_price"], event["guests"], event.get("nonprofit", False))
    return total_booked

def largest_event(events: list) -> str:
    """Return the client of the event with the largest event total"""
    largest_client = ""
    largest_total = None
    for event in events:
        total = calculate_event_total(event["guest_price"], event["guests"], event.get("nonprofit", False))
        if largest_total is None or total > largest_total:
            largest_total = total
            largest_client = event["client"]
    return largest_client

def format_event_line(client: str, total: float, signoff: bool, second_chef: bool) -> str:
    """Return one line report for event details"""
    signoff_text = "yes" if signoff else "no"
    chef_text = "yes" if second_chef else "no"
    return (f"{client}: ${total:.2f} | sign-off: {signoff_text} | second chef: {chef_text}")