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
    levelsensor = await server.nodes.base_object_type.add_object_type(idx, "LevelSensor")
    await (await levelsensor.add_variable(idx, "Minimal Level", False)).set_modelling_rule(True)
    level_sensor = await server.nodes.objects.add_object(idx, "Level Sensor", levelsensor)
    level_sensor.set_writable()

    temperaturesensor = await server.nodes.base_object_type.add_object_type(idx, "temperaturesensor")
    await (await temperaturesensor.add_variable(idx, "Temperature", 52.4)).set_modelling_rule(True)
    temperature_sensor = await server.nodes.objects.add_object(idx, "Temperature Sensor", temperaturesensor)
    temperature_sensor.set_writable()

    vectordata = await server.nodes.base_object_type.add_object_type(idx, "vectordata")
    await (await vectordata.add_variable(idx, "Vector Data",[1.4, 1.2, 3.9, False])).set_modelling_rule(True)
    vector_data = await server.nodes.objects.add_object(idx, "Vector Data", vectordata)
    vector_data.set_writable()

    time = await server.nodes.base_object_type.add_object_type(idx, "vectordata")
    await (await time.add_variable(idx, "Work Time", 31.99)).set_modelling_rule(True)
    work_time = await server.nodes.objects.add_object(idx, "Work Time", time)
    work_time.set_writable()

    ekstruder_variable = await server.nodes.base_object_type.add_object_type(idx, "Ekstruder Value")
    await (await ekstruder_variable.add_variable(idx, "Ekstruder Value", [1000, 22.1, 54.2,])).set_modelling_rule(True)
    ekstruder_array = await server.nodes.objects.add_object(idx, "Ekstruder Value", ekstruder_variable)
    ekstruder_array.set_writable()

    pistonrod = await server.nodes.base_object_type.add_object_type(idx, "Piston Rod")
    await (await pistonrod.add_variable(idx, "Piston Rod", False)).set_modelling_rule(True)
    piston_value = await server.nodes.objects.add_object(idx, "Piston Rod", pistonrod)
    piston_value.set_writable()

    pumppressure = await server.nodes.base_object_type.add_object_type(idx, "Pump Pressure")
    await (await pumppressure.add_variable(idx, "Pump Pressure", 800)).set_modelling_rule(True)
    pump_pressure = await server.nodes.objects.add_object(idx, "Pump Pressure", pumppressure)
    pump_pressure.set_writable()

    actuatorposition = await server.nodes.base_object_type.add_object_type(idx, "Actuator Position")
    await (await actuatorposition.add_variable(idx, "Actuator Position", 2)).set_modelling_rule(True)
    actuator_position = await server.nodes.objects.add_object(idx, "Actuator Position", actuatorposition)
    actuator_position.set_writable()

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
