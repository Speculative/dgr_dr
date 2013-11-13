"""
# Copyright 2013 Jeffrey Tao, Maxwell Huang-Hobbs, William Saulnier, 2013
# Distributed under the terms of the GNU General Public License.
#
# This file is part of Dgr_dr
#
# This is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this file.  If not, see <http://www.gnu.org/licenses/>.
"""

from flask import Flask  
app = Flask(__name__)  
from app import views