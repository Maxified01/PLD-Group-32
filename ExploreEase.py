import random

class ExploreEase:
    def __init__(self):
        self.destinations = {
            "Kigali": {
                "description": "The capital and largest city of Rwanda, known for its clean streets and hilly landscape.",
                "attractions": ["Kigali Genocide Memorial", "Kimironko Market", "Inema Art Center"],
                "activities": ["Nyamirambo Walking Tour", "Visit Akagera National Park", "Explore Mount Kigali"],
                "restaurants": ["Repub Lounge", "Heaven Restaurant & Bar", "Poivre Noir"]
            },
            "Lagos": {
                "description": "The largest city in Nigeria, known for its vibrant culture, music, and bustling markets.",
                "attractions": ["Lekki Conservation Centre", "Nike Art Gallery", "Tarkwa Bay Beach"],
                "activities": ["Shop at Balogun Market", "Visit Freedom Park", "Explore Lekki Arts & Crafts Market"],
                "restaurants": ["Nok by Alara", "Yellow Chilli", "Cafe Neo"]
            }
            # Add more destinations here
        }
        self.user_preferences = {
            "activities": ["Cultural Sightseeing", "Adventure Sports", "Cuisine Exploration"],
            "budget": ["Budget", "Mid-range", "Luxury"]
        }

    def display_destinations(self):
        print("\nAvailable Destinations:")
        for destination in self.destinations:
            print(destination)

    def get_destination_info(self, destination):
        info = self.destinations.get(destination)
        if info:
            print(f"\nDestination: {destination}")
            print(f"Description: {info['description']}")
            print("\nPopular Attractions:")
            for attraction in info['attractions']:
                print(f"- {attraction}")
            print("\nRecommended Activities:")
            for activity in info['activities']:
                print(f"- {activity}")
            print("\nTop Restaurants:")
            for restaurant in info['restaurants']:
                print(f"- {restaurant}")
        else:
            print("Destination not found.")

    def recommend_destination(self, preferences):
        print("\nRecommended Destination based on your preferences:")
        destination = random.choice(list(self.destinations.keys()))
        print(destination)

    def plan_trip(self):
        print("\nTrip Planning Tools:")
        destination = input("Enter destination: ")
        self.get_destination_info(destination)
        # Additional trip planning logic can be added here

    def explore_local_insights(self):
        print("\nLocal Insights:")
        # Placeholder for local insights feature
        print("Connect with local guides and experts.")

    def display_menu(self):
        print("\nMenu:")
        print("1. Explore Destinations")
        print("2. Plan Trip")
        print("3. Get Personalized Recommendations")
        print("4. Explore Local Insights")
        print("5. Exit")

    def main(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")

            if choice == '1':
                self.display_destinations()
            elif choice == '2':
                self.plan_trip()
            elif choice == '3':
                preferences = self.get_user_preferences()
                self.recommend_destination(preferences)
            elif choice == '4':
                self.explore_local_insights()
            elif choice == '5':
                print("Exiting ExploreEase. Thank you for using!")
                break
            else:
                print("Invalid choice. Please enter a valid option.")

    def get_user_preferences(self):
        preferences = {}
        print("\nPlease provide your preferences:")
        for category, options in self.user_preferences.items():
            print(f"\n{category}:")
            for i, option in enumerate(options, start=1):
                print(f"{i}. {option}")
            choice = input(f"Choose {category} (1-{len(options)}): ")
            preferences[category] = options[int(choice) - 1]
        return preferences

if __name__ == "__main__":
    explore_ease_app = ExploreEase()
    explore_ease_app.main()

