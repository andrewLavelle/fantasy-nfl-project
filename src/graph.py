import matplotlib.pyplot as plt

def extract_data(data):
    years_to_points = data["data"]
    years = sorted(years_to_points.keys())
    points = [years_to_points[year] for year in years]

    return years, points

def plot_data(data):
    # Need to extract data into x and y axis
    x_years, y_pts = extract_data(data)

    plt.plot(x_years, y_pts)
    plt.xlabel("Season")
    plt.ylabel("Fantasy Points")
    plt.title(f"{data["player"]} - Fantasy Points by Season")
    plt.show()