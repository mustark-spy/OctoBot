#  This file is part of OctoBot (https://github.com/Drakkar-Software/OctoBot)
#  Copyright (c) 2023 Drakkar-Software, All rights reserved.
#
#  OctoBot is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either
#  version 3.0 of the License, or (at your option) any later version.
#
#  OctoBot is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#  General Public License for more details.
#
#  You should have received a copy of the GNU General Public
#  License along with OctoBot. If not, see <https://www.gnu.org/licenses/>.
import sys

from octobot.cli import main
import octobot_commons.constants

# Redéfinition dynamique AVANT le démarrage d'OctoBot
octobot_commons.constants.USER_FOLDER = "/data/user"
octobot_commons.constants.TENTACLES_FOLDER = "/data/tentacles"

if __name__ == '__main__':
    main(sys.argv[1:])
