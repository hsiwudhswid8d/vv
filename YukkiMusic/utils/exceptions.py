#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/hsiwudhswid8d >.
#
# This file is part of < https://github.com/hsiwudhswid8d/vv > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/hsiwudhswid8d/vv/LICENSE >
#
# All rights reserved.


class AssistantErr(Exception):
    def __init__(self, errr: str):
        super().__init__(errr)
