"""This program helps to plan a tea party based on the number of guests."""

__author__: str = "730669352"


def main_planner(guests: int) -> None:
    """This function is the entrypoint of the program."""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )


def tea_bags(people: int) -> int:
    """the function computes the number of tea bags needed"""
    return people * 2


def treats(people: int) -> int:
    """the function finds how many treats needed based on number of teas"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """the function determines the cost of combined treats and tea bags"""
    return tea_count * 0.50 + treat_count * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party?")))
