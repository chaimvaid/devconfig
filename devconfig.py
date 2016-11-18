from evdev import InputDevice, categorize, ecodes, UInput, list_devices, ecodes as e

devices = [InputDevice(fn) for fn in list_devices()]
for device in devices:
    if device.name == 'Microsoft Microsoft® Comfort Mouse 4500':
        print(device.fn, device.name, device.phys)
        dev = InputDevice(device.fn)

        print(dev)
        
        dev.grab()
        
        mouse = UInput.from_device(dev)
        for event in dev.read_loop():
            c = categorize(event)
            
            if event.code == 275 and c.keystate == c.key_down:
                try:
                    print(categorize(event))
                    ui = UInput()
                    ui.write(ecodes.EV_KEY, ecodes.KEY_LEFTCTRL, 1)
                    ui.write(ecodes.EV_KEY, ecodes.KEY_C, 1)
                    ui.write(ecodes.EV_KEY, ecodes.KEY_LEFTCTRL, 0)
                    ui.write(ecodes.EV_KEY, ecodes.KEY_C, 0)
                    ui.syn()
                    ui.close()
                    
                except:
                    pass
            elif event.code == 276 and c.keystate == c.key_down:
                try:
                    print(categorize(event))
                    ui = UInput()
                    ui.write(ecodes.EV_KEY, ecodes.KEY_LEFTCTRL, 1)
                    ui.write(ecodes.EV_KEY, ecodes.KEY_V, 1)
                    ui.write(ecodes.EV_KEY, ecodes.KEY_LEFTCTRL, 0)
                    ui.write(ecodes.EV_KEY, ecodes.KEY_V, 0)
                    ui.syn()
                    ui.close()
                    
                except:
                    pass
            elif event.code == 6:
                event.code = 8
                print(categorize(event))
                
                mouse.write_event(event)
                mouse.write_event(event)
                mouse.write_event(event)
                mouse.syn()
            elif event.code != 275 and event.code != 276:
                print(categorize(event))
                mouse.write_event(event)
                mouse.syn()
                
                
