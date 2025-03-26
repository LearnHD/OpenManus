import pytest
from unittest.mock import patch, MagicMock
import sys
import os
import signal
from main import start_backend, start_frontend, stop_servers, cleanup, signal_handler

def test_start_backend():
    with patch('subprocess.Popen') as mock_popen:
        mock_process = MagicMock()
        mock_popen.return_value = mock_process
        
        assert start_backend() == True
        mock_popen.assert_called_once()

def test_start_frontend():
    with patch('subprocess.Popen') as mock_popen, \
         patch('os.chdir') as mock_chdir:
        mock_process = MagicMock()
        mock_popen.return_value = mock_process
        
        assert start_frontend() == True
        mock_popen.assert_called_once()
        assert mock_chdir.call_count == 2

def test_stop_servers():
    with patch('main.cleanup') as mock_cleanup:
        assert stop_servers() == True
        mock_cleanup.assert_called_once()

def test_cleanup():
    with patch('main.backend_process') as mock_backend, \
         patch('main.frontend_process') as mock_frontend:
        mock_backend.terminate = MagicMock()
        mock_frontend.terminate = MagicMock()
        
        cleanup()
        
        mock_backend.terminate.assert_called_once()
        mock_frontend.terminate.assert_called_once()

def test_signal_handler():
    with patch('main.cleanup') as mock_cleanup, \
         patch('sys.exit') as mock_exit:
        signal_handler(signal.SIGTERM, None)
        
        mock_cleanup.assert_called_once()
        mock_exit.assert_called_once_with(0)