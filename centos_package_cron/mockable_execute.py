# coding: utf8


import subprocess


class MockableExecute(object):
    def run_command(self,command,command_input=None):
        proc = subprocess.Popen(command, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
        out = proc.communicate(input=command_input)[0]
        return out


