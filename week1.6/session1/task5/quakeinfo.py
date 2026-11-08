from feed import QuakeFeed
from dataset import QuakeDataset

level = input("Enter significance level (e.g. 4.5): ").strip()
period = input("Enter time period (e.g. week): ").strip()

feed = QuakeFeed(level, period)
dataset = QuakeDataset(feed)

dataset.read_feed()

print(dataset)                                    
print(f"Mean depth = {dataset.mean_depth():.2f} km")
print(f"Mean magnitude = {dataset.mean_magnitude():.1f}")

strongest = dataset.strongest_quake()
print()
print(f"Strongest quake occurred at {strongest.time.strftime('%H:%M:%S')} "
      f"on {strongest.time.strftime('%Y-%m-%d')}")
print(f"at {strongest.longitude}° longitude, {strongest.latitude}° latitude")
print(f"The depth was {strongest.depth} km")
print(f"The magnitude was {strongest.magnitude}")