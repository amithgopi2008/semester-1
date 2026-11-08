from data import Dataset

filename = input("Enter the name of a data file: ")

dataset = Dataset(filename)

print(f"\nDataset size: {len(dataset)}")
print(f"Mean:         {dataset.mean():.2f}")
print(f"Median:       {dataset.median():.2f}")

print("\nValues:")
for value in dataset:
    print(value)