from dbus_next.aio.message_bus import MessageBus
import asyncio

loop = asyncio.get_event_loop()

async def main():
    bus = await MessageBus().connect()
    introspection = await bus.introspect('com.canonical.Unity', '/com/canonical/Unity/Session')
    obj = bus.get_proxy_object('com.canonical.Unity', '/com/canonical/Unity/Session', introspection)
    
    print(obj.introspection.interfaces)
    
    await loop.create_future()
    
loop.run_until_complete(main())

# import asyncio
# from typing import Callable
# import dbus_next
# from dbus_next.aio.message_bus import MessageBus
# from dbus_next import Variant

# def handler(message):
#     print(message)


# async def Dbus():

#     bus = await MessageBus().connect()
    
#     if bus.connected:
#         print('Bus is connected at: ','bus name-> ',bus.unique_name, 'bus adress-> ',bus._bus_address)
#         bus.
#         bus.add_message_handler(handler)
        
        
        

# asyncio.run(Dbus())

# import subprocess

# screen = subprocess.run( 'gdbus', 'call', '-e', '-d', 'com.canonical.Unity', '-o', '/com/canonical/Unity/Session', '-m', 'com.canonical.Unity.Session.IsLocked', '|', 'grep', '-ioP', '"(true)|(false)"')
# print(screen)
# import dbus_next

# dbus_next.


# from dbus.mainloop.glib import DBusGMainLoop


# def filter_cb(bus, message):
#     if message.get_member() != "ActiveChanged":
#         return
#     args = message.get_args_list()
#     if args[0] == True:
#         print("Lock Screen")
#     else:
#         print("Unlock Screen")

# DBusGMainLoop(set_as_default=True)
# bus = dbus.SessionBus()
# bus.add_match_string("type='signal',interface='org.gnome.ScreenSaver'")
# bus.add_message_filter(filter_cb)


# while True:
#     screen = subprocess.run(['gsettings', 'get', 'org.gnome.desktop.lockdown', 'disable-lock-screen'])
#     print(screen)