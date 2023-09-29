import value_return

# Calculate the hour, minutes, and seconds using the functions
hour = value_return.get_hour(3800)
minutes = value_return.get_minutes(3800)
seconds = value_return.get_seconds(3800)

# Format the time using an f-string
time = f"{hour:02d}:{minutes:02d}:{seconds:02d}"

# Print the formatted time
print(time)