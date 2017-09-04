#! /usr/bin/python3

__version__ = "1.0"

from ctypes import *
lib = CDLL("libopi_wrapper.so")

def SysTypeText():
	func = lib.SysTypeText
	func.restype = c_char_p
	return func()

def SerialNumber():
	func = lib.SerialNumber
	func.restype = c_char_p
	return func()
	
def StorageDevice():
	func = lib.StorageDevice
	func.restype = c_char_p
	return func()
	

def StorageDeviceBlock():
	func = lib.StorageDeviceBlock
	func.restype = c_char_p
	return func()

def StorageDevicePartition():
	func = lib.StorageDevicePartition
	func.restype = c_char_p
	return func()


def NetworkDevice():
	func = lib.NetworkDevice
	func.restype = c_char_p
	return func()

def isArmada():
	func = lib.SysTypeText
	func.restype = c_char_p
	return func()
	return lib.isArmada(None) > 0

def isOpi():
	func = lib.SysTypeText
	func.restype = c_char_p
	return func()
	return lib.isOpi(None) > 0

def isXu4():
	func = lib.SysTypeText
	func.restype = c_char_p
	return func()
	return lib.isXu4(None) > 0

def isOlimexA20():
	func = lib.SysTypeText
	func.restype = c_char_p
	return func()
	return lib.isOlimexA20(None) > 0

def isPC():
	func = lib.SysTypeText
	func.restype = c_char_p
	return func()
	return lib.isPC(None) > 0

# For testing only
if __name__ == '__main__':
	print( SysTypeText() );
	print( SerialNumber() );
	print( StorageDevice() );
	print( StorageDeviceBlock() );
	print( StorageDevicePartition() );
	print( NetworkDevice() );
	

	print( isArmada() );
	print( isOpi() );
	print( isXu4() );
	print( isOlimexA20() );
	print( isPC() );
   
   

