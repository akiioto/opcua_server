'''
   Show 3 different examples for creating an object:
   1) create a basic object
   2) create a new object type and a instance of the new object type
   3) import a new object from xml address space and create a instance of the new object type
'''
import sys
sys.path.insert(0, "..")
import asyncio
import copy
import logging
from datetime import datetime
import time
from math import sin
import asyncua

from asyncua import ua, Server


async def main():

    # setup our server
    server = Server()
    await server.init()

    server.set_endpoint("opc.tcp://0.0.0.0:4840/freeopcua/server/")

    # setup our own namespace, not really necessary but should as spec
    uri = "http://examples.freeopcua.github.io"
    idx = await server.register_namespace(uri)

    # create a new node type we can instantiate in our address space
    levelsensor = await server.nodes.objects.add_oadd_objectject_type(idx, "LevelSensor")
    level_sensor = await levelsensor.add_variable(idx, "Level Sensor", False)
    await level_sensor.set_writable()

    temperaturesensor = await server.nodes.objects.add_object(idx, "Temperature Sensor")
    temperature_sensor = await temperaturesensor.add_variable(idx, "Temperature Sensor", 52.4)
    await temperature_sensor.set_writable()

    vectordata = await server.nodes.objects.add_object(idx, "Vector Data")
    vector_data = await vectordata.add_variable(idx, "Vector Data", [1.4, 1.2, 3.9, False])
    await vector_data.set_writable()

    time = await server.nodes.objects.add_object(idx, "Time")
    work_time = await time.add_variable(idx, "Work Time", 31.99)
    await work_time.set_writable()

    ekstruder_variable = await server.nodes.objects.add_object(idx, "Ekstruder Value")
    ekstruder_array = await ekstruder_variable.add_variable(idx, "Ekstruder Value", [1.4, 1.2, 3.9])
    await ekstruder_array.set_writable()

    pistonrod = await server.nodes.objects.add_object(idx, "Piston Rod")
    piston_value = await pistonrod.add_variable(idx, "Piston Rod", False)
    await piston_value.set_writable()

    pumppressure = await server.nodes.objects.add_object(idx, "Pump Pressure")
    pump_pressure = await pumppressure.add_variable(idx, "Pump Pressure", 800)
    await pump_pressure.set_writable()

    actuatorposition = await server.nodes.objects.add_object(idx, "Actuator Position")
    actuator_position = await actuatorposition.add_variable(idx, "Actuator Position", 2)
    await actuator_position.set_writable()

    # create directly some objects and variables
    myobj = await server.nodes.objects.add_object(idx, "MyObject")
    myvar = await myobj.add_variable(idx, "MyVariable", 6.7)
    await myvar.set_writable()  # Set MyVariable to be writable by clients
    mystringvar = await myobj.add_variable(idx, "MyStringVariable", "Really nice string")
    await mystringvar.set_writable()  # Set MyVariable to be writable by clients
    mydtvar = await myobj.add_variable(idx, "MyDateTimeVar", datetime.utcnow())
    await mydtvar.set_writable()  # Set MyVariable to be writable by clients
    myarrayvar = await myobj.add_variable(idx, "myarrayvar", [6.7, 7.9])
    myuintvar = await myobj.add_variable(idx, "myuintvar", ua.UInt16(4))
    await myobj.add_variable(idx, "myStronglytTypedVariable", ua.Variant([], ua.VariantType.UInt32))
    await myarrayvar.set_writable(True)
    myprop = await myobj.add_property(idx, "myproperty", "I am a property")
   
   # starting!



    async with server:
        while True:
            await asyncio.sleep(1)


if __name__ == "__main__":
    asyncio.run(main())
