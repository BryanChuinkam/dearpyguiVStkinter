import tkinter as tk
import tkinter.font
from tkinter import colorchooser
from PIL import Image, ImageTk
from resources.horoscopeUtility import get_horoscope, get_top_three

scale_factor = 1


def print_me():
    print("Works")


def pick_color():
    color = colorchooser.askcolor()[1]
    print(color)


def create_plot():  # 24 lines
    top_3_zodiac = get_top_three()
    # Define the data points
    data = [top_3_zodiac[0][1], top_3_zodiac[1][1], top_3_zodiac[2][1]]

    c_width = 1000 * scale_factor  # Define it's width
    c_height = 200 * scale_factor  # Define it's height
    c = tk.Canvas(root, width=c_width, height=c_height, bg='white')
    c.grid(row=5, column=1, padx=5*scale_factor, pady=5*scale_factor)

    # The variables below size the bar graph
    y_stretch = 15 * scale_factor  # The highest y = max_data_value * y_stretch
    y_gap = 5 * scale_factor  # The gap between lower canvas edge and x axis
    x_stretch = 10 * scale_factor  # Stretch x wide enough to fit the variables
    x_width = 25 * scale_factor  # The width of the x-axis
    x_gap = 5 * scale_factor  # The gap between left canvas edge and y axis

    colors = ['red', 'green', 'blue']

    # A quick for loop to calculate the rectangle
    for index, count in enumerate(data):
        # coordinates of each bar
        # Bottom left coordinate
        x0 = index * x_stretch + index * x_width + x_gap
        # Top left coordinates
        y0 = c_height - (count * y_stretch + y_gap)
        # Bottom right coordinates
        x1 = index * x_stretch + index * x_width + x_width + x_gap
        # Top right coordinates
        y1 = c_height - y_gap
        # Draw the bar
        c.create_rectangle(x0, y0, x1, y1, fill=f"{colors[index]}")
        # Put the y value above the bar
        c.create_text(x0 + 4 * scale_factor, y0, anchor=tk.SW, text=str(count), font=default_font)  # had to add default_font here

    # create plot legend
    legend_text = f"""---------------------------\n|red: {top_3_zodiac[0][0]} |\n|green: {top_3_zodiac[1][0]} |\n|blue: {top_3_zodiac[2][0]}|\n---------------------------"""
    legend_frame = tk.Frame(root, height=1*scale_factor, width=1*scale_factor)
    legend_frame.grid(row=5, column=1, padx=5*scale_factor, pady=5*scale_factor)
    legend_label = tk.Label(legend_frame, text=legend_text, bg='white')
    legend_label.grid(row=0, column=0)


def set_horoscope():  # 19
    """calls get_horoscope function which returns horoscope object.
       displays results to GUI
    """
    zodiac_label, horoscope = get_horoscope(int(day_entry.get()), int(month_entry.get()))
    horoscope_text = horoscope['horoscope']

    try:
        # destroy all widgets from frame
        for widget in frame.winfo_children():
            widget.destroy()
    except Exception as e:
        pass

    frame.grid(row=4, columnspan=3, padx=5*scale_factor, pady=2*scale_factor)
    # add horoscope and zodiac label and zodiac image to GUI
    zodiac_label_tk = tk.Label(frame, text=zodiac_label, )
    zodiac_label_tk.grid(row=0, columnspan=3, padx=5*scale_factor, pady=2*scale_factor)

    # Load and display an image
    global image
    image = Image.open(f"..{horoscope['zodiac_sign']}")
    image = image.resize((400 * scale_factor, 200 * scale_factor))
    image = ImageTk.PhotoImage(image)
    image_label = tk.Label(frame, image=image)
    image_label.grid(row=1, column=0, padx=5*scale_factor, pady=2*scale_factor)

    horoscope = tk.Text(frame, height=5 * scale_factor, width=30*scale_factor, wrap='word', )
    horoscope.grid(row=1, column=2, columnspan=2, padx=5*scale_factor, pady=2*scale_factor)
    horoscope.insert(tk.END, horoscope_text)


# Create the main window
root = tk.Tk()
root.title("Horoscope")
root.attributes("-fullscreen", True)

frame = tk.Frame(root)

# Create an object of type Font from tkinter.
default_font = tkinter.font.Font(family="../resources/HappyMonkey-Regular.ttf", size=25*scale_factor)
root.option_add("*Font", default_font)

# Create a menubar. 16 lines of code (not counting white spaces which make code more readable)
menubar = tk.Menu()
root.config(menu=menubar)  # Insert the menubar in the main window.
# Create the 'file' menu.
file_menu = tk.Menu(menubar, tearoff=False)
file_menu.add_command(label="Save", command=print_me)
file_menu.add_command(label="Save As", command=print_me)

settings_menu = tk.Menu(menubar, tearoff=False)
settings_menu.add_command(label="Setting 1", command=print_me)
settings_menu.add_command(label="Setting 2", command=print_me)

menubar.add_cascade(menu=file_menu, label="File", )  # Append the menu to the menubar.
file_menu.add_cascade(menu=settings_menu, label="Settings", )

help_menu = tk.Menu(menubar, tearoff=False)
menubar.add_cascade(menu=help_menu, label="Help", command=print_me)

widget_items_menu = tk.Menu(menubar, tearoff=False, postcommand=pick_color)
menubar.add_cascade(menu=widget_items_menu, label="Other Widget Items", )

# Create input fields
day_label = tk.Label(root, text="Day:", )
day_label.grid(row=0, column=0, padx=5*scale_factor, pady=2*scale_factor)
day_entry = tk.Spinbox(root, from_=1, to=31, )  # need callback function for data validation
day_entry.grid(row=0, column=1, padx=5*scale_factor, pady=2*scale_factor)

month_label = tk.Label(root, text="Month:", )
month_label.grid(row=1, column=0, padx=5*scale_factor, pady=2*scale_factor)
month_entry = tk.Spinbox(root, from_=1, to=12, )
month_entry.grid(row=1, column=1, padx=5*scale_factor, pady=2*scale_factor)

# Create calculate button
calculate_button = tk.Button(root, text="Today's Horoscope", command=set_horoscope, )
calculate_button.grid(row=3, column=1, padx=5*scale_factor, pady=2*scale_factor)

# Create Plot button
calculate_button = tk.Button(root, text="Plot", command=create_plot, )
calculate_button.grid(row=3, column=2, padx=5*scale_factor, pady=2*scale_factor)

# Run Tkinter main loop
root.mainloop()
