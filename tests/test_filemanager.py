from menu import list_folder_content, create_folder, sys_info, app_creator
import os

def test_list_folder_content():
    test_data = os.listdir(os.getcwd())
    assert list_folder_content() == test_data

def test_sys_info():
    assert  sys_info() =='Windows-10-10.0.19045-SP0'

def test_app_creator():
    assert app_creator() == 'Пицуков Михаил'