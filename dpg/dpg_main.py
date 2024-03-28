import dearpygui.dearpygui as dpg
from resources.horoscopeUtility import get_horoscope, get_top_three

scale_factor = 1


def print_me():
    print("Works")


def create_plot(): # 10 lines
    top_3_zodiac = get_top_three()
    with dpg.plot(label="Frequency of Top three zodiac signs", height=200*scale_factor, width=-1, parent="primary window"):
        dpg.add_plot_legend()
        # create x axis
        dpg.add_plot_axis(dpg.mvXAxis, label="Top Three Zodiacs",  no_tick_labels=True)
        dpg.set_axis_limits(dpg.last_item(), 9, 33)

        # create y axis
        with dpg.plot_axis(dpg.mvYAxis, label="Count"):
            dpg.set_axis_limits(dpg.last_item(), 0, 10)
            dpg.add_bar_series([20], [top_3_zodiac[0][1]], label=f"{top_3_zodiac[0][0]}", weight=1)
            dpg.add_bar_series([21], [top_3_zodiac[1][1]], label=f"{top_3_zodiac[1][0]}", weight=1)
            dpg.add_bar_series([22], [top_3_zodiac[2][1]], label=f"{top_3_zodiac[2][0]}", weight=1)


def set_horoscope():
    """calls get_horoscope function which returns horoscope object.
       displays results to GUI
    """
    zodiac_label, horoscope = get_horoscope(dpg.get_value("Day"), dpg.get_value("Month"))

    try:
        dpg.delete_item('results_row')
        dpg.delete_item('zodiac_label_row')
        # add image
        width, height, channels, data = dpg.load_image(f"..{horoscope['zodiac_sign']}")
        with dpg.texture_registry(show=False):
            dpg.add_static_texture(width=width, height=height, default_value=data, tag=f"{zodiac_label}_zodiac_img")
    except Exception as e:
        pass

    # add horoscope and zodiac label and zodiac image to GUI
    with dpg.table_row(parent='display_table', tag='zodiac_label_row'):
        dpg.add_spacer()
        dpg.add_text(zodiac_label.upper(), pos=[375*scale_factor, 250*scale_factor], tag="zodiac_label")
        dpg.add_spacer()
    with dpg.table_row(parent='display_table', tag='results_row'):
        dpg.add_spacer()
        with dpg.group(horizontal=True):
            dpg.add_image(f"{zodiac_label}_zodiac_img", height=400 * scale_factor, width=400*scale_factor)
            dpg.add_text(horoscope['horoscope'], wrap=800, indent=500*scale_factor, tag="Horoscope")
        dpg.add_spacer()


dpg.create_context()  # Allows access to DPG commands


# add custom font then bind it to all items in app
with dpg.font_registry():
    default_font = dpg.add_font("../resources/HappyMonkey-Regular.ttf", 25*scale_factor)
dpg.bind_font(default_font)

dpg.create_viewport(title='Horoscope')  # window created by OS
# Create the main window
with dpg.window(label="Horoscope", tag="primary window"):
    # Create a menubar. 10 lines of code
    with dpg.menu_bar():
        with dpg.menu(label="File"):
            dpg.add_menu_item(label="Save", callback=print_me)
            dpg.add_menu_item(label="Save As", callback=print_me)
            with dpg.menu(label="Settings"):
                dpg.add_menu_item(label="Setting 1", callback=print_me, check=True)
                dpg.add_menu_item(label="Setting 2", callback=print_me)
        dpg.add_menu_item(label="Help", callback=print_me)
        with dpg.menu(label="Other Widget Items"):
            dpg.add_color_picker(label="Pick Color", callback=print_me)
    # Create input fields
    with dpg.table(header_row=False, resizable=False, tag='display_table'):
        dpg.add_table_column(width_fixed=False, init_width_or_weight=10)
        dpg.add_table_column(width_fixed=False, init_width_or_weight=80)
        dpg.add_table_column(width_fixed=False, init_width_or_weight=10)
        with dpg.table_row():
            dpg.add_spacer()
            with dpg.group(horizontal=False):
                dpg.add_input_int(label="Day", min_value=1, max_value=31, min_clamped=True, default_value=1, max_clamped=True, tag="Day")
                dpg.add_input_int(label="Month", min_value=1, max_value=12, min_clamped=True, default_value=1, max_clamped=True, tag="Month")
                with dpg.group(horizontal=True):
                    dpg.add_button(label="Today's Horoscope", callback=set_horoscope)
                    dpg.add_button(label="Plot", callback=create_plot, indent=500*scale_factor)
            dpg.add_spacer()


# Run the Dear PyGui app
dpg.set_primary_window("primary window", True)
dpg.setup_dearpygui()  # Assign the viewport
dpg.show_viewport(maximized=True)  # show the viewport
dpg.start_dearpygui()  # handles render loop
dpg.destroy_context()  # Proper clean up of DPG
