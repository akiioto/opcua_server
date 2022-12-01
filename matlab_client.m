clc
clear all 
UaClient = opcua('localhost', 4840);

UaClient.connect();

UaClient