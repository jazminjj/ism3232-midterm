"""Tests for the Harvest Table Catering business rules."""

from business_rules import (
    calculate_event_total,
    calculate_food_cost,
    format_event_line,
    get_event_discount,
    needs_signoff,
    needs_second_chef,
    total_booked,
    largest_event
)

def test_calculate_food_cost():
    assert round(calculate_food_cost(20.00, 10), 2) == 200.00

def test_discount_below_25_guests():
    assert get_event_discount(20) == 0.0

def test_discount_at_25_guests():
    assert get_event_discount(25) == 0.05

def test_discount_at_99_guests():
    assert get_event_discount(99) == 0.05

def test_discount_for_nonprofit():
    assert get_event_discount(100, nonprofit=True) == 0.12

def test_discount_for_nonprofit_below_100_guests():
    assert get_event_discount(40, nonprofit=True) == 0.05

def test_total_has_five_percent_discount_at_25_guests():
    assert round(calculate_event_total(40.0, 25), 2) == 950.00

def test_total_has_no_fee_when_discounted_total_exceeds_500():
    assert round(calculate_event_total(500.01, 1), 2) == 500.01

def test_nonprofit_true_changes_discount_at_100_guests():
    regular = round(calculate_event_total(30.0, 100, False), 2)
    nonprofit = round(calculate_event_total(30.0, 100, True), 2)
    assert regular == 2850.0
    assert nonprofit == 2640.0

def test_signoff_not_needed_at_2500():
    assert needs_signoff(2500.0) is False

def test_signoff_needed_at_2500_01():
    assert needs_signoff(2500.01) is True

def test_second_chef_not_needed_just_under_3000_total():
    assert needs_second_chef(10, 2999.99) is False


def test_second_chef_needed_at_exactly_3000_total():
    assert needs_second_chef(10, 3000.0) is True


# total_booked
def test_total_booked_adds_every_event_total():
    events = [
        {"client": "A", "guest_price": 18.0, "guests": 20},
        {"client": "B", "guest_price": 40.0, "guests": 25},
    ]
    assert round(total_booked(events), 2) == 1385.0


def test_total_booked_empty_list_is_zero():
    assert round(total_booked([]), 2) == 0.0


# largest_event
def test_largest_event_returns_client_with_biggest_total():
    events = [
        {"client": "A", "guest_price": 18.0, "guests": 20},
        {"client": "B", "guest_price": 40.0, "guests": 25},
    ]
    assert largest_event(events) == "B"


def test_largest_event_tie_returns_first_in_list():
    events = [
        {"client": "First", "guest_price": 40.0, "guests": 25},
        {"client": "Second", "guest_price": 40.0, "guests": 25},
    ]
    assert largest_event(events) == "First"


def test_largest_event_empty_list_returns_empty_string():
    assert largest_event([]) == ""


# format_event_line
def test_format_event_line_shows_no_for_false_values():
    line = format_event_line("Finch Law", 435, False, False)
    assert line == "Finch Law: $435.00 | sign-off: no | second chef: no"


def test_format_event_line_shows_yes_and_two_decimals():
    line = format_event_line("Lumen Labs", 1154.25, True, True) 