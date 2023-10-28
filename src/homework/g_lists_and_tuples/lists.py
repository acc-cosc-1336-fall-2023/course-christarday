#
def add_inventory(widget, widget_name, quantity):
    if widget_name in widget: 
         widget[widget_name] += quantity
    else:
        widget[widget_name] =  quantity

def remove_inventory_widget(widget, widget_name):
    if widget_name in widget:
        del widget[widget_name]
        return "Record Deleted"
    else:
        return "Item Not Found"

