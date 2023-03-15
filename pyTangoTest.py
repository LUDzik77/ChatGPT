#quickly done script (not tested)
import PyTango
# create a DeviceProxy object for the Tango device
device_proxy = PyTango.DeviceProxy("tango://localhost:10000/my/device")

def choose_attribute():
    while True:
        attribute = input("Input attribute name to change: ")
        try:
            attribute_value = device_proxy.read_attribute(attribute).value
            print(f"{attribute} value: ", attribute_value)
            return(attribute)
        except:
            print("wrong name of the dive attribute")
        
    
def change_attribute_value(att_with_value_to_change):
    while True:
        new_value = input(f"Enter new value for {att_with_value_to_change}: ")
        try:
            device_proxy.write_attribute(attribute , new_value)
            new_attribute_value = device_proxy.read_attribute(att_with_value_to_change).value
            print(f"New value for {att_with_value_to_change}: ", new_attribute_value)
            return(input("Click any key to close the script"))
        except:
            print("impossible to change the value")        
            

if __name__ == "__main__":
    att_with_value_to_change = choose_attribute()
    change_attribute_value(att_with_value_to_change)
