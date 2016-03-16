# -*- coding: utf-8 -*-
'''
Copyright (c) 2016, Virginia Tech
All rights reserved.
Redistribution and use in source and binary forms, with or without modification, are permitted provided that the
 following conditions are met:
1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following
disclaimer.
2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following
disclaimer in the documentation and/or other materials provided with the distribution.
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES,
INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
The views and conclusions contained in the software and documentation are those of the authors and should not be
interpreted as representing official policies, either expressed or implied, of the FreeBSD Project.
This material was prepared as an account of work sponsored by an agency of the United States Government. Neither the
United States Government nor the United States Department of Energy, nor Virginia Tech, nor any of their employees,
nor any jurisdiction or organization that has cooperated in the development of these materials, makes any warranty,
express or implied, or assumes any legal liability or responsibility for the accuracy, completeness, or usefulness or
any information, apparatus, product, software, or process disclosed, or represents that its use would not infringe
privately owned rights.
Reference herein to any specific commercial product, process, or service by trade name, trademark, manufacturer, or
otherwise does not necessarily constitute or imply its endorsement, recommendation, favoring by the United States
Government or any agency thereof, or Virginia Tech - Advanced Research Institute. The views and opinions of authors
expressed herein do not necessarily state or reflect those of the United States Government or any agency thereof.
VIRGINIA TECH – ADVANCED RESEARCH INSTITUTE
under Contract DE-EE0006352
#__author__ = "BEMOSS Team"
#__credits__ = ""
#__version__ = "2.0"
#__maintainer__ = "BEMOSS Team"
#__email__ = "aribemoss@gmail.com"
#__website__ = "www.bemoss.org"
#__created__ = "2014-09-12 12:04:50"
#__lastUpdated__ = "2016-03-14 11:23:33"
'''

import subprocess

def agent_status(passwd):
    cmd = 'echo \'' + str(passwd) + '\' | sudo -S ~/workspace/bemoss_os/env/bin/volttron-ctl status'
    try:
        output = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE).communicate()[0]
        return output
    except Exception as er:
        print er
        print('Failure @ agent_status in volttronFunc.')

def start_agent(passwd, agent_id, type=1):
    try:
        if type == 1:
            # Start agent by id (The first column in agent view), this is for start agent who has not been repackaged.
            cmd = 'echo \'' + str(passwd) + '\' | sudo -S ~/workspace/bemoss_os/env/bin/volttron-ctl start ' + str(agent_id)
        else:
            # Start agent by tag, since after repackage, the agent id will change.
            cmd = 'echo \'' + str(passwd) + '\' | sudo -S ~/workspace/bemoss_os/env/bin/volttron-ctl start --tag ' + str(agent_id)
        subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    except Exception as er:
        print er
        print('Failure @ start_agent in volttronFunc')

def stop_agent(passwd, agent_id):
    try:
        cmd = 'echo \'' + str(passwd) + '\' | sudo -S ~/workspace/bemoss_os/env/bin/volttron-ctl stop ' + str(agent_id)
        subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    except Exception as er:
        print er
        print('Failure @ stop_agent in volttronFunc')

def remove_agent(passwd, agent_id):
    try:
        cmd = 'echo \'' + str(passwd) + '\' | sudo -S ~/workspace/bemoss_os/env/bin/volttron-ctl remove ' + str(agent_id)
        subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    except Exception as er:
        print er
        print('Failure @ remove_agent in volttronFunc')

def clear_agent(passwd):
    try:
        cmd = 'echo \'' + str(passwd) + '\' | sudo -S ~/workspace/bemoss_os/env/bin/volttron-ctl clear'
        subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    except Exception as er:
        print er
        print('Failure @ clear_agent in volttronFunc')

def repackage_agent(passwd, agentType):
    try:
        cmd = 'echo \'' + str(passwd) + '\' | sudo -S ~/workspace/bemoss_os/env/bin/volttron-pkg package ~/workspace/bemoss_os/Agents/' + str(agentType)
        output = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE).communicate()[0]
        return output
    except Exception as er:
        print er
        print('Failure @ repackage_agent in volttronFunc')


def configure_agent(passwd, agent_id, agentType):
    try:
        cmd = 'echo \'' + str(passwd) + '\' | sudo -S ~/workspace/bemoss_os/env/bin/volttron-pkg configure /tmp/volttron_wheels/' + agentType.lower() + '-0.1-py2-none-any.whl ~/workspace/bemoss_os/Agents/LaunchFiles/' + str(agent_id) + '.launch.json'
        subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    except Exception as er:
        print er
        print('Failure @ configure_agent in volttronFunc')


def install_agent(passwd, agent_id, agentType):
    try:
        cmd = 'echo \'' + str(passwd) + '\' | sudo -S ~/workspace/bemoss_os/env/bin/volttron-ctl install ' + str(agent_id) + '=/tmp/volttron_wheels/' + agentType.lower() + '-0.1-py2-none-any.whl'
        subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    except Exception as er:
        print er
        print('Failure @ install_agent in volttronFunc')

