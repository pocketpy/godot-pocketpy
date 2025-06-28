from enum import Enum




class Side(Enum):

    SIDE_LEFT: 'int' = 0
    SIDE_TOP: 'int' = 1
    SIDE_RIGHT: 'int' = 2
    SIDE_BOTTOM: 'int' = 3




class Corner(Enum):

    CORNER_TOP_LEFT: 'int' = 0
    CORNER_TOP_RIGHT: 'int' = 1
    CORNER_BOTTOM_RIGHT: 'int' = 2
    CORNER_BOTTOM_LEFT: 'int' = 3




class Orientation(Enum):

    VERTICAL: 'int' = 1
    HORIZONTAL: 'int' = 0




class ClockDirection(Enum):

    CLOCKWISE: 'int' = 0
    COUNTERCLOCKWISE: 'int' = 1




class HorizontalAlignment(Enum):

    HORIZONTAL_ALIGNMENT_LEFT: 'int' = 0
    HORIZONTAL_ALIGNMENT_CENTER: 'int' = 1
    HORIZONTAL_ALIGNMENT_RIGHT: 'int' = 2
    HORIZONTAL_ALIGNMENT_FILL: 'int' = 3




class VerticalAlignment(Enum):

    VERTICAL_ALIGNMENT_TOP: 'int' = 0
    VERTICAL_ALIGNMENT_CENTER: 'int' = 1
    VERTICAL_ALIGNMENT_BOTTOM: 'int' = 2
    VERTICAL_ALIGNMENT_FILL: 'int' = 3




class InlineAlignment(Enum):

    INLINE_ALIGNMENT_TOP_TO: 'int' = 0
    INLINE_ALIGNMENT_CENTER_TO: 'int' = 1
    INLINE_ALIGNMENT_BASELINE_TO: 'int' = 3
    INLINE_ALIGNMENT_BOTTOM_TO: 'int' = 2
    INLINE_ALIGNMENT_TO_TOP: 'int' = 0
    INLINE_ALIGNMENT_TO_CENTER: 'int' = 4
    INLINE_ALIGNMENT_TO_BASELINE: 'int' = 8
    INLINE_ALIGNMENT_TO_BOTTOM: 'int' = 12
    INLINE_ALIGNMENT_TOP: 'int' = 0
    INLINE_ALIGNMENT_CENTER: 'int' = 5
    INLINE_ALIGNMENT_BOTTOM: 'int' = 14
    INLINE_ALIGNMENT_IMAGE_MASK: 'int' = 3
    INLINE_ALIGNMENT_TEXT_MASK: 'int' = 12




class EulerOrder(Enum):

    EULER_ORDER_XYZ: 'int' = 0
    EULER_ORDER_XZY: 'int' = 1
    EULER_ORDER_YXZ: 'int' = 2
    EULER_ORDER_YZX: 'int' = 3
    EULER_ORDER_ZXY: 'int' = 4
    EULER_ORDER_ZYX: 'int' = 5




class Key(Enum):

    KEY_NONE: 'int' = 0
    KEY_SPECIAL: 'int' = 4194304
    KEY_ESCAPE: 'int' = 4194305
    KEY_TAB: 'int' = 4194306
    KEY_BACKTAB: 'int' = 4194307
    KEY_BACKSPACE: 'int' = 4194308
    KEY_ENTER: 'int' = 4194309
    KEY_KP_ENTER: 'int' = 4194310
    KEY_INSERT: 'int' = 4194311
    KEY_DELETE: 'int' = 4194312
    KEY_PAUSE: 'int' = 4194313
    KEY_PRINT: 'int' = 4194314
    KEY_SYSREQ: 'int' = 4194315
    KEY_CLEAR: 'int' = 4194316
    KEY_HOME: 'int' = 4194317
    KEY_END: 'int' = 4194318
    KEY_LEFT: 'int' = 4194319
    KEY_UP: 'int' = 4194320
    KEY_RIGHT: 'int' = 4194321
    KEY_DOWN: 'int' = 4194322
    KEY_PAGEUP: 'int' = 4194323
    KEY_PAGEDOWN: 'int' = 4194324
    KEY_SHIFT: 'int' = 4194325
    KEY_CTRL: 'int' = 4194326
    KEY_META: 'int' = 4194327
    KEY_ALT: 'int' = 4194328
    KEY_CAPSLOCK: 'int' = 4194329
    KEY_NUMLOCK: 'int' = 4194330
    KEY_SCROLLLOCK: 'int' = 4194331
    KEY_F1: 'int' = 4194332
    KEY_F2: 'int' = 4194333
    KEY_F3: 'int' = 4194334
    KEY_F4: 'int' = 4194335
    KEY_F5: 'int' = 4194336
    KEY_F6: 'int' = 4194337
    KEY_F7: 'int' = 4194338
    KEY_F8: 'int' = 4194339
    KEY_F9: 'int' = 4194340
    KEY_F10: 'int' = 4194341
    KEY_F11: 'int' = 4194342
    KEY_F12: 'int' = 4194343
    KEY_F13: 'int' = 4194344
    KEY_F14: 'int' = 4194345
    KEY_F15: 'int' = 4194346
    KEY_F16: 'int' = 4194347
    KEY_F17: 'int' = 4194348
    KEY_F18: 'int' = 4194349
    KEY_F19: 'int' = 4194350
    KEY_F20: 'int' = 4194351
    KEY_F21: 'int' = 4194352
    KEY_F22: 'int' = 4194353
    KEY_F23: 'int' = 4194354
    KEY_F24: 'int' = 4194355
    KEY_F25: 'int' = 4194356
    KEY_F26: 'int' = 4194357
    KEY_F27: 'int' = 4194358
    KEY_F28: 'int' = 4194359
    KEY_F29: 'int' = 4194360
    KEY_F30: 'int' = 4194361
    KEY_F31: 'int' = 4194362
    KEY_F32: 'int' = 4194363
    KEY_F33: 'int' = 4194364
    KEY_F34: 'int' = 4194365
    KEY_F35: 'int' = 4194366
    KEY_KP_MULTIPLY: 'int' = 4194433
    KEY_KP_DIVIDE: 'int' = 4194434
    KEY_KP_SUBTRACT: 'int' = 4194435
    KEY_KP_PERIOD: 'int' = 4194436
    KEY_KP_ADD: 'int' = 4194437
    KEY_KP_0: 'int' = 4194438
    KEY_KP_1: 'int' = 4194439
    KEY_KP_2: 'int' = 4194440
    KEY_KP_3: 'int' = 4194441
    KEY_KP_4: 'int' = 4194442
    KEY_KP_5: 'int' = 4194443
    KEY_KP_6: 'int' = 4194444
    KEY_KP_7: 'int' = 4194445
    KEY_KP_8: 'int' = 4194446
    KEY_KP_9: 'int' = 4194447
    KEY_MENU: 'int' = 4194370
    KEY_HYPER: 'int' = 4194371
    KEY_HELP: 'int' = 4194373
    KEY_BACK: 'int' = 4194376
    KEY_FORWARD: 'int' = 4194377
    KEY_STOP: 'int' = 4194378
    KEY_REFRESH: 'int' = 4194379
    KEY_VOLUMEDOWN: 'int' = 4194380
    KEY_VOLUMEMUTE: 'int' = 4194381
    KEY_VOLUMEUP: 'int' = 4194382
    KEY_MEDIAPLAY: 'int' = 4194388
    KEY_MEDIASTOP: 'int' = 4194389
    KEY_MEDIAPREVIOUS: 'int' = 4194390
    KEY_MEDIANEXT: 'int' = 4194391
    KEY_MEDIARECORD: 'int' = 4194392
    KEY_HOMEPAGE: 'int' = 4194393
    KEY_FAVORITES: 'int' = 4194394
    KEY_SEARCH: 'int' = 4194395
    KEY_STANDBY: 'int' = 4194396
    KEY_OPENURL: 'int' = 4194397
    KEY_LAUNCHMAIL: 'int' = 4194398
    KEY_LAUNCHMEDIA: 'int' = 4194399
    KEY_LAUNCH0: 'int' = 4194400
    KEY_LAUNCH1: 'int' = 4194401
    KEY_LAUNCH2: 'int' = 4194402
    KEY_LAUNCH3: 'int' = 4194403
    KEY_LAUNCH4: 'int' = 4194404
    KEY_LAUNCH5: 'int' = 4194405
    KEY_LAUNCH6: 'int' = 4194406
    KEY_LAUNCH7: 'int' = 4194407
    KEY_LAUNCH8: 'int' = 4194408
    KEY_LAUNCH9: 'int' = 4194409
    KEY_LAUNCHA: 'int' = 4194410
    KEY_LAUNCHB: 'int' = 4194411
    KEY_LAUNCHC: 'int' = 4194412
    KEY_LAUNCHD: 'int' = 4194413
    KEY_LAUNCHE: 'int' = 4194414
    KEY_LAUNCHF: 'int' = 4194415
    KEY_GLOBE: 'int' = 4194416
    KEY_KEYBOARD: 'int' = 4194417
    KEY_JIS_EISU: 'int' = 4194418
    KEY_JIS_KANA: 'int' = 4194419
    KEY_UNKNOWN: 'int' = 8388607
    KEY_SPACE: 'int' = 32
    KEY_EXCLAM: 'int' = 33
    KEY_QUOTEDBL: 'int' = 34
    KEY_NUMBERSIGN: 'int' = 35
    KEY_DOLLAR: 'int' = 36
    KEY_PERCENT: 'int' = 37
    KEY_AMPERSAND: 'int' = 38
    KEY_APOSTROPHE: 'int' = 39
    KEY_PARENLEFT: 'int' = 40
    KEY_PARENRIGHT: 'int' = 41
    KEY_ASTERISK: 'int' = 42
    KEY_PLUS: 'int' = 43
    KEY_COMMA: 'int' = 44
    KEY_MINUS: 'int' = 45
    KEY_PERIOD: 'int' = 46
    KEY_SLASH: 'int' = 47
    KEY_0: 'int' = 48
    KEY_1: 'int' = 49
    KEY_2: 'int' = 50
    KEY_3: 'int' = 51
    KEY_4: 'int' = 52
    KEY_5: 'int' = 53
    KEY_6: 'int' = 54
    KEY_7: 'int' = 55
    KEY_8: 'int' = 56
    KEY_9: 'int' = 57
    KEY_COLON: 'int' = 58
    KEY_SEMICOLON: 'int' = 59
    KEY_LESS: 'int' = 60
    KEY_EQUAL: 'int' = 61
    KEY_GREATER: 'int' = 62
    KEY_QUESTION: 'int' = 63
    KEY_AT: 'int' = 64
    KEY_A: 'int' = 65
    KEY_B: 'int' = 66
    KEY_C: 'int' = 67
    KEY_D: 'int' = 68
    KEY_E: 'int' = 69
    KEY_F: 'int' = 70
    KEY_G: 'int' = 71
    KEY_H: 'int' = 72
    KEY_I: 'int' = 73
    KEY_J: 'int' = 74
    KEY_K: 'int' = 75
    KEY_L: 'int' = 76
    KEY_M: 'int' = 77
    KEY_N: 'int' = 78
    KEY_O: 'int' = 79
    KEY_P: 'int' = 80
    KEY_Q: 'int' = 81
    KEY_R: 'int' = 82
    KEY_S: 'int' = 83
    KEY_T: 'int' = 84
    KEY_U: 'int' = 85
    KEY_V: 'int' = 86
    KEY_W: 'int' = 87
    KEY_X: 'int' = 88
    KEY_Y: 'int' = 89
    KEY_Z: 'int' = 90
    KEY_BRACKETLEFT: 'int' = 91
    KEY_BACKSLASH: 'int' = 92
    KEY_BRACKETRIGHT: 'int' = 93
    KEY_ASCIICIRCUM: 'int' = 94
    KEY_UNDERSCORE: 'int' = 95
    KEY_QUOTELEFT: 'int' = 96
    KEY_BRACELEFT: 'int' = 123
    KEY_BAR: 'int' = 124
    KEY_BRACERIGHT: 'int' = 125
    KEY_ASCIITILDE: 'int' = 126
    KEY_YEN: 'int' = 165
    KEY_SECTION: 'int' = 167




class KeyModifierMask(Enum):

    KEY_CODE_MASK: 'int' = 8388607
    KEY_MODIFIER_MASK: 'int' = 2130706432
    KEY_MASK_CMD_OR_CTRL: 'int' = 16777216
    KEY_MASK_SHIFT: 'int' = 33554432
    KEY_MASK_ALT: 'int' = 67108864
    KEY_MASK_META: 'int' = 134217728
    KEY_MASK_CTRL: 'int' = 268435456
    KEY_MASK_KPAD: 'int' = 536870912
    KEY_MASK_GROUP_SWITCH: 'int' = 1073741824




class KeyLocation(Enum):

    KEY_LOCATION_UNSPECIFIED: 'int' = 0
    KEY_LOCATION_LEFT: 'int' = 1
    KEY_LOCATION_RIGHT: 'int' = 2




class MouseButton(Enum):

    MOUSE_BUTTON_NONE: 'int' = 0
    MOUSE_BUTTON_LEFT: 'int' = 1
    MOUSE_BUTTON_RIGHT: 'int' = 2
    MOUSE_BUTTON_MIDDLE: 'int' = 3
    MOUSE_BUTTON_WHEEL_UP: 'int' = 4
    MOUSE_BUTTON_WHEEL_DOWN: 'int' = 5
    MOUSE_BUTTON_WHEEL_LEFT: 'int' = 6
    MOUSE_BUTTON_WHEEL_RIGHT: 'int' = 7
    MOUSE_BUTTON_XBUTTON1: 'int' = 8
    MOUSE_BUTTON_XBUTTON2: 'int' = 9




class MouseButtonMask(Enum):

    MOUSE_BUTTON_MASK_LEFT: 'int' = 1
    MOUSE_BUTTON_MASK_RIGHT: 'int' = 2
    MOUSE_BUTTON_MASK_MIDDLE: 'int' = 4
    MOUSE_BUTTON_MASK_MB_XBUTTON1: 'int' = 128
    MOUSE_BUTTON_MASK_MB_XBUTTON2: 'int' = 256




class JoyButton(Enum):

    JOY_BUTTON_INVALID: 'int' = -1
    JOY_BUTTON_A: 'int' = 0
    JOY_BUTTON_B: 'int' = 1
    JOY_BUTTON_X: 'int' = 2
    JOY_BUTTON_Y: 'int' = 3
    JOY_BUTTON_BACK: 'int' = 4
    JOY_BUTTON_GUIDE: 'int' = 5
    JOY_BUTTON_START: 'int' = 6
    JOY_BUTTON_LEFT_STICK: 'int' = 7
    JOY_BUTTON_RIGHT_STICK: 'int' = 8
    JOY_BUTTON_LEFT_SHOULDER: 'int' = 9
    JOY_BUTTON_RIGHT_SHOULDER: 'int' = 10
    JOY_BUTTON_DPAD_UP: 'int' = 11
    JOY_BUTTON_DPAD_DOWN: 'int' = 12
    JOY_BUTTON_DPAD_LEFT: 'int' = 13
    JOY_BUTTON_DPAD_RIGHT: 'int' = 14
    JOY_BUTTON_MISC1: 'int' = 15
    JOY_BUTTON_PADDLE1: 'int' = 16
    JOY_BUTTON_PADDLE2: 'int' = 17
    JOY_BUTTON_PADDLE3: 'int' = 18
    JOY_BUTTON_PADDLE4: 'int' = 19
    JOY_BUTTON_TOUCHPAD: 'int' = 20
    JOY_BUTTON_SDL_MAX: 'int' = 21
    JOY_BUTTON_MAX: 'int' = 128




class JoyAxis(Enum):

    JOY_AXIS_INVALID: 'int' = -1
    JOY_AXIS_LEFT_X: 'int' = 0
    JOY_AXIS_LEFT_Y: 'int' = 1
    JOY_AXIS_RIGHT_X: 'int' = 2
    JOY_AXIS_RIGHT_Y: 'int' = 3
    JOY_AXIS_TRIGGER_LEFT: 'int' = 4
    JOY_AXIS_TRIGGER_RIGHT: 'int' = 5
    JOY_AXIS_SDL_MAX: 'int' = 6
    JOY_AXIS_MAX: 'int' = 10




class MIDIMessage(Enum):

    MIDI_MESSAGE_NONE: 'int' = 0
    MIDI_MESSAGE_NOTE_OFF: 'int' = 8
    MIDI_MESSAGE_NOTE_ON: 'int' = 9
    MIDI_MESSAGE_AFTERTOUCH: 'int' = 10
    MIDI_MESSAGE_CONTROL_CHANGE: 'int' = 11
    MIDI_MESSAGE_PROGRAM_CHANGE: 'int' = 12
    MIDI_MESSAGE_CHANNEL_PRESSURE: 'int' = 13
    MIDI_MESSAGE_PITCH_BEND: 'int' = 14
    MIDI_MESSAGE_SYSTEM_EXCLUSIVE: 'int' = 240
    MIDI_MESSAGE_QUARTER_FRAME: 'int' = 241
    MIDI_MESSAGE_SONG_POSITION_POINTER: 'int' = 242
    MIDI_MESSAGE_SONG_SELECT: 'int' = 243
    MIDI_MESSAGE_TUNE_REQUEST: 'int' = 246
    MIDI_MESSAGE_TIMING_CLOCK: 'int' = 248
    MIDI_MESSAGE_START: 'int' = 250
    MIDI_MESSAGE_CONTINUE: 'int' = 251
    MIDI_MESSAGE_STOP: 'int' = 252
    MIDI_MESSAGE_ACTIVE_SENSING: 'int' = 254
    MIDI_MESSAGE_SYSTEM_RESET: 'int' = 255




class Error(Enum):

    OK: 'int' = 0
    FAILED: 'int' = 1
    ERR_UNAVAILABLE: 'int' = 2
    ERR_UNCONFIGURED: 'int' = 3
    ERR_UNAUTHORIZED: 'int' = 4
    ERR_PARAMETER_RANGE_ERROR: 'int' = 5
    ERR_OUT_OF_MEMORY: 'int' = 6
    ERR_FILE_NOT_FOUND: 'int' = 7
    ERR_FILE_BAD_DRIVE: 'int' = 8
    ERR_FILE_BAD_PATH: 'int' = 9
    ERR_FILE_NO_PERMISSION: 'int' = 10
    ERR_FILE_ALREADY_IN_USE: 'int' = 11
    ERR_FILE_CANT_OPEN: 'int' = 12
    ERR_FILE_CANT_WRITE: 'int' = 13
    ERR_FILE_CANT_READ: 'int' = 14
    ERR_FILE_UNRECOGNIZED: 'int' = 15
    ERR_FILE_CORRUPT: 'int' = 16
    ERR_FILE_MISSING_DEPENDENCIES: 'int' = 17
    ERR_FILE_EOF: 'int' = 18
    ERR_CANT_OPEN: 'int' = 19
    ERR_CANT_CREATE: 'int' = 20
    ERR_QUERY_FAILED: 'int' = 21
    ERR_ALREADY_IN_USE: 'int' = 22
    ERR_LOCKED: 'int' = 23
    ERR_TIMEOUT: 'int' = 24
    ERR_CANT_CONNECT: 'int' = 25
    ERR_CANT_RESOLVE: 'int' = 26
    ERR_CONNECTION_ERROR: 'int' = 27
    ERR_CANT_ACQUIRE_RESOURCE: 'int' = 28
    ERR_CANT_FORK: 'int' = 29
    ERR_INVALID_DATA: 'int' = 30
    ERR_INVALID_PARAMETER: 'int' = 31
    ERR_ALREADY_EXISTS: 'int' = 32
    ERR_DOES_NOT_EXIST: 'int' = 33
    ERR_DATABASE_CANT_READ: 'int' = 34
    ERR_DATABASE_CANT_WRITE: 'int' = 35
    ERR_COMPILATION_FAILED: 'int' = 36
    ERR_METHOD_NOT_FOUND: 'int' = 37
    ERR_LINK_FAILED: 'int' = 38
    ERR_SCRIPT_FAILED: 'int' = 39
    ERR_CYCLIC_LINK: 'int' = 40
    ERR_INVALID_DECLARATION: 'int' = 41
    ERR_DUPLICATE_SYMBOL: 'int' = 42
    ERR_PARSE_ERROR: 'int' = 43
    ERR_BUSY: 'int' = 44
    ERR_SKIP: 'int' = 45
    ERR_HELP: 'int' = 46
    ERR_BUG: 'int' = 47
    ERR_PRINTER_ON_FIRE: 'int' = 48




class PropertyHint(Enum):

    PROPERTY_HINT_NONE: 'int' = 0
    PROPERTY_HINT_RANGE: 'int' = 1
    PROPERTY_HINT_ENUM: 'int' = 2
    PROPERTY_HINT_ENUM_SUGGESTION: 'int' = 3
    PROPERTY_HINT_EXP_EASING: 'int' = 4
    PROPERTY_HINT_LINK: 'int' = 5
    PROPERTY_HINT_FLAGS: 'int' = 6
    PROPERTY_HINT_LAYERS_2D_RENDER: 'int' = 7
    PROPERTY_HINT_LAYERS_2D_PHYSICS: 'int' = 8
    PROPERTY_HINT_LAYERS_2D_NAVIGATION: 'int' = 9
    PROPERTY_HINT_LAYERS_3D_RENDER: 'int' = 10
    PROPERTY_HINT_LAYERS_3D_PHYSICS: 'int' = 11
    PROPERTY_HINT_LAYERS_3D_NAVIGATION: 'int' = 12
    PROPERTY_HINT_LAYERS_AVOIDANCE: 'int' = 37
    PROPERTY_HINT_FILE: 'int' = 13
    PROPERTY_HINT_DIR: 'int' = 14
    PROPERTY_HINT_GLOBAL_FILE: 'int' = 15
    PROPERTY_HINT_GLOBAL_DIR: 'int' = 16
    PROPERTY_HINT_RESOURCE_TYPE: 'int' = 17
    PROPERTY_HINT_MULTILINE_TEXT: 'int' = 18
    PROPERTY_HINT_EXPRESSION: 'int' = 19
    PROPERTY_HINT_PLACEHOLDER_TEXT: 'int' = 20
    PROPERTY_HINT_COLOR_NO_ALPHA: 'int' = 21
    PROPERTY_HINT_OBJECT_ID: 'int' = 22
    PROPERTY_HINT_TYPE_STRING: 'int' = 23
    PROPERTY_HINT_NODE_PATH_TO_EDITED_NODE: 'int' = 24
    PROPERTY_HINT_OBJECT_TOO_BIG: 'int' = 25
    PROPERTY_HINT_NODE_PATH_VALID_TYPES: 'int' = 26
    PROPERTY_HINT_SAVE_FILE: 'int' = 27
    PROPERTY_HINT_GLOBAL_SAVE_FILE: 'int' = 28
    PROPERTY_HINT_INT_IS_OBJECTID: 'int' = 29
    PROPERTY_HINT_INT_IS_POINTER: 'int' = 30
    PROPERTY_HINT_ARRAY_TYPE: 'int' = 31
    PROPERTY_HINT_DICTIONARY_TYPE: 'int' = 38
    PROPERTY_HINT_LOCALE_ID: 'int' = 32
    PROPERTY_HINT_LOCALIZABLE_STRING: 'int' = 33
    PROPERTY_HINT_NODE_TYPE: 'int' = 34
    PROPERTY_HINT_HIDE_QUATERNION_EDIT: 'int' = 35
    PROPERTY_HINT_PASSWORD: 'int' = 36
    PROPERTY_HINT_TOOL_BUTTON: 'int' = 39
    PROPERTY_HINT_ONESHOT: 'int' = 40
    PROPERTY_HINT_MAX: 'int' = 42




class PropertyUsageFlags(Enum):

    PROPERTY_USAGE_NONE: 'int' = 0
    PROPERTY_USAGE_STORAGE: 'int' = 2
    PROPERTY_USAGE_EDITOR: 'int' = 4
    PROPERTY_USAGE_INTERNAL: 'int' = 8
    PROPERTY_USAGE_CHECKABLE: 'int' = 16
    PROPERTY_USAGE_CHECKED: 'int' = 32
    PROPERTY_USAGE_GROUP: 'int' = 64
    PROPERTY_USAGE_CATEGORY: 'int' = 128
    PROPERTY_USAGE_SUBGROUP: 'int' = 256
    PROPERTY_USAGE_CLASS_IS_BITFIELD: 'int' = 512
    PROPERTY_USAGE_NO_INSTANCE_STATE: 'int' = 1024
    PROPERTY_USAGE_RESTART_IF_CHANGED: 'int' = 2048
    PROPERTY_USAGE_SCRIPT_VARIABLE: 'int' = 4096
    PROPERTY_USAGE_STORE_IF_NULL: 'int' = 8192
    PROPERTY_USAGE_UPDATE_ALL_IF_MODIFIED: 'int' = 16384
    PROPERTY_USAGE_SCRIPT_DEFAULT_VALUE: 'int' = 32768
    PROPERTY_USAGE_CLASS_IS_ENUM: 'int' = 65536
    PROPERTY_USAGE_NIL_IS_VARIANT: 'int' = 131072
    PROPERTY_USAGE_ARRAY: 'int' = 262144
    PROPERTY_USAGE_ALWAYS_DUPLICATE: 'int' = 524288
    PROPERTY_USAGE_NEVER_DUPLICATE: 'int' = 1048576
    PROPERTY_USAGE_HIGH_END_GFX: 'int' = 2097152
    PROPERTY_USAGE_NODE_PATH_FROM_SCENE_ROOT: 'int' = 4194304
    PROPERTY_USAGE_RESOURCE_NOT_PERSISTENT: 'int' = 8388608
    PROPERTY_USAGE_KEYING_INCREMENTS: 'int' = 16777216
    PROPERTY_USAGE_DEFERRED_SET_RESOURCE: 'int' = 33554432
    PROPERTY_USAGE_EDITOR_INSTANTIATE_OBJECT: 'int' = 67108864
    PROPERTY_USAGE_EDITOR_BASIC_SETTING: 'int' = 134217728
    PROPERTY_USAGE_READ_ONLY: 'int' = 268435456
    PROPERTY_USAGE_SECRET: 'int' = 536870912
    PROPERTY_USAGE_DEFAULT: 'int' = 6
    PROPERTY_USAGE_NO_EDITOR: 'int' = 2




class MethodFlags(Enum):

    METHOD_FLAG_NORMAL: 'int' = 1
    METHOD_FLAG_EDITOR: 'int' = 2
    METHOD_FLAG_CONST: 'int' = 4
    METHOD_FLAG_VIRTUAL: 'int' = 8
    METHOD_FLAG_VARARG: 'int' = 16
    METHOD_FLAG_STATIC: 'int' = 32
    METHOD_FLAG_OBJECT_CORE: 'int' = 64
    METHOD_FLAG_VIRTUAL_REQUIRED: 'int' = 128
    METHOD_FLAGS_DEFAULT: 'int' = 1




class Variant__Type(Enum):

    TYPE_NIL: 'int' = 0
    TYPE_BOOL: 'int' = 1
    TYPE_INT: 'int' = 2
    TYPE_FLOAT: 'int' = 3
    TYPE_STRING: 'int' = 4
    TYPE_VECTOR2: 'int' = 5
    TYPE_VECTOR2I: 'int' = 6
    TYPE_RECT2: 'int' = 7
    TYPE_RECT2I: 'int' = 8
    TYPE_VECTOR3: 'int' = 9
    TYPE_VECTOR3I: 'int' = 10
    TYPE_TRANSFORM2D: 'int' = 11
    TYPE_VECTOR4: 'int' = 12
    TYPE_VECTOR4I: 'int' = 13
    TYPE_PLANE: 'int' = 14
    TYPE_QUATERNION: 'int' = 15
    TYPE_AABB: 'int' = 16
    TYPE_BASIS: 'int' = 17
    TYPE_TRANSFORM3D: 'int' = 18
    TYPE_PROJECTION: 'int' = 19
    TYPE_COLOR: 'int' = 20
    TYPE_STRING_NAME: 'int' = 21
    TYPE_NODE_PATH: 'int' = 22
    TYPE_RID: 'int' = 23
    TYPE_OBJECT: 'int' = 24
    TYPE_CALLABLE: 'int' = 25
    TYPE_SIGNAL: 'int' = 26
    TYPE_DICTIONARY: 'int' = 27
    TYPE_ARRAY: 'int' = 28
    TYPE_PACKED_BYTE_ARRAY: 'int' = 29
    TYPE_PACKED_INT32_ARRAY: 'int' = 30
    TYPE_PACKED_INT64_ARRAY: 'int' = 31
    TYPE_PACKED_FLOAT32_ARRAY: 'int' = 32
    TYPE_PACKED_FLOAT64_ARRAY: 'int' = 33
    TYPE_PACKED_STRING_ARRAY: 'int' = 34
    TYPE_PACKED_VECTOR2_ARRAY: 'int' = 35
    TYPE_PACKED_VECTOR3_ARRAY: 'int' = 36
    TYPE_PACKED_COLOR_ARRAY: 'int' = 37
    TYPE_PACKED_VECTOR4_ARRAY: 'int' = 38
    TYPE_MAX: 'int' = 39




class Variant__Operator(Enum):

    OP_EQUAL: 'int' = 0
    OP_NOT_EQUAL: 'int' = 1
    OP_LESS: 'int' = 2
    OP_LESS_EQUAL: 'int' = 3
    OP_GREATER: 'int' = 4
    OP_GREATER_EQUAL: 'int' = 5
    OP_ADD: 'int' = 6
    OP_SUBTRACT: 'int' = 7
    OP_MULTIPLY: 'int' = 8
    OP_DIVIDE: 'int' = 9
    OP_NEGATE: 'int' = 10
    OP_POSITIVE: 'int' = 11
    OP_MODULE: 'int' = 12
    OP_POWER: 'int' = 13
    OP_SHIFT_LEFT: 'int' = 14
    OP_SHIFT_RIGHT: 'int' = 15
    OP_BIT_AND: 'int' = 16
    OP_BIT_OR: 'int' = 17
    OP_BIT_XOR: 'int' = 18
    OP_BIT_NEGATE: 'int' = 19
    OP_AND: 'int' = 20
    OP_OR: 'int' = 21
    OP_XOR: 'int' = 22
    OP_NOT: 'int' = 23
    OP_IN: 'int' = 24
    OP_MAX: 'int' = 25




class AESContext__Mode(Enum):

    MODE_ECB_ENCRYPT: 'int' = 0
    MODE_ECB_DECRYPT: 'int' = 1
    MODE_CBC_ENCRYPT: 'int' = 2
    MODE_CBC_DECRYPT: 'int' = 3
    MODE_MAX: 'int' = 4




class AStarGrid2D__Heuristic(Enum):

    HEURISTIC_EUCLIDEAN: 'int' = 0
    HEURISTIC_MANHATTAN: 'int' = 1
    HEURISTIC_OCTILE: 'int' = 2
    HEURISTIC_CHEBYSHEV: 'int' = 3
    HEURISTIC_MAX: 'int' = 4




class AStarGrid2D__DiagonalMode(Enum):

    DIAGONAL_MODE_ALWAYS: 'int' = 0
    DIAGONAL_MODE_NEVER: 'int' = 1
    DIAGONAL_MODE_AT_LEAST_ONE_WALKABLE: 'int' = 2
    DIAGONAL_MODE_ONLY_IF_NO_OBSTACLES: 'int' = 3
    DIAGONAL_MODE_MAX: 'int' = 4




class AStarGrid2D__CellShape(Enum):

    CELL_SHAPE_SQUARE: 'int' = 0
    CELL_SHAPE_ISOMETRIC_RIGHT: 'int' = 1
    CELL_SHAPE_ISOMETRIC_DOWN: 'int' = 2
    CELL_SHAPE_MAX: 'int' = 3




class Animation__TrackType(Enum):

    TYPE_VALUE: 'int' = 0
    TYPE_POSITION_3D: 'int' = 1
    TYPE_ROTATION_3D: 'int' = 2
    TYPE_SCALE_3D: 'int' = 3
    TYPE_BLEND_SHAPE: 'int' = 4
    TYPE_METHOD: 'int' = 5
    TYPE_BEZIER: 'int' = 6
    TYPE_AUDIO: 'int' = 7
    TYPE_ANIMATION: 'int' = 8




class Animation__InterpolationType(Enum):

    INTERPOLATION_NEAREST: 'int' = 0
    INTERPOLATION_LINEAR: 'int' = 1
    INTERPOLATION_CUBIC: 'int' = 2
    INTERPOLATION_LINEAR_ANGLE: 'int' = 3
    INTERPOLATION_CUBIC_ANGLE: 'int' = 4




class Animation__UpdateMode(Enum):

    UPDATE_CONTINUOUS: 'int' = 0
    UPDATE_DISCRETE: 'int' = 1
    UPDATE_CAPTURE: 'int' = 2




class Animation__LoopMode(Enum):

    LOOP_NONE: 'int' = 0
    LOOP_LINEAR: 'int' = 1
    LOOP_PINGPONG: 'int' = 2




class Animation__LoopedFlag(Enum):

    LOOPED_FLAG_NONE: 'int' = 0
    LOOPED_FLAG_END: 'int' = 1
    LOOPED_FLAG_START: 'int' = 2




class Animation__FindMode(Enum):

    FIND_MODE_NEAREST: 'int' = 0
    FIND_MODE_APPROX: 'int' = 1
    FIND_MODE_EXACT: 'int' = 2




class AnimationMixer__AnimationCallbackModeProcess(Enum):

    ANIMATION_CALLBACK_MODE_PROCESS_PHYSICS: 'int' = 0
    ANIMATION_CALLBACK_MODE_PROCESS_IDLE: 'int' = 1
    ANIMATION_CALLBACK_MODE_PROCESS_MANUAL: 'int' = 2




class AnimationMixer__AnimationCallbackModeMethod(Enum):

    ANIMATION_CALLBACK_MODE_METHOD_DEFERRED: 'int' = 0
    ANIMATION_CALLBACK_MODE_METHOD_IMMEDIATE: 'int' = 1




class AnimationMixer__AnimationCallbackModeDiscrete(Enum):

    ANIMATION_CALLBACK_MODE_DISCRETE_DOMINANT: 'int' = 0
    ANIMATION_CALLBACK_MODE_DISCRETE_RECESSIVE: 'int' = 1
    ANIMATION_CALLBACK_MODE_DISCRETE_FORCE_CONTINUOUS: 'int' = 2




class AnimationNode__FilterAction(Enum):

    FILTER_IGNORE: 'int' = 0
    FILTER_PASS: 'int' = 1
    FILTER_STOP: 'int' = 2
    FILTER_BLEND: 'int' = 3




class AnimationNodeAnimation__PlayMode(Enum):

    PLAY_MODE_FORWARD: 'int' = 0
    PLAY_MODE_BACKWARD: 'int' = 1




class AnimationNodeBlendSpace1D__BlendMode(Enum):

    BLEND_MODE_INTERPOLATED: 'int' = 0
    BLEND_MODE_DISCRETE: 'int' = 1
    BLEND_MODE_DISCRETE_CARRY: 'int' = 2




class AnimationNodeBlendSpace2D__BlendMode(Enum):

    BLEND_MODE_INTERPOLATED: 'int' = 0
    BLEND_MODE_DISCRETE: 'int' = 1
    BLEND_MODE_DISCRETE_CARRY: 'int' = 2




class AnimationNodeOneShot__OneShotRequest(Enum):

    ONE_SHOT_REQUEST_NONE: 'int' = 0
    ONE_SHOT_REQUEST_FIRE: 'int' = 1
    ONE_SHOT_REQUEST_ABORT: 'int' = 2
    ONE_SHOT_REQUEST_FADE_OUT: 'int' = 3




class AnimationNodeOneShot__MixMode(Enum):

    MIX_MODE_BLEND: 'int' = 0
    MIX_MODE_ADD: 'int' = 1




class AnimationNodeStateMachine__StateMachineType(Enum):

    STATE_MACHINE_TYPE_ROOT: 'int' = 0
    STATE_MACHINE_TYPE_NESTED: 'int' = 1
    STATE_MACHINE_TYPE_GROUPED: 'int' = 2




class AnimationNodeStateMachineTransition__SwitchMode(Enum):

    SWITCH_MODE_IMMEDIATE: 'int' = 0
    SWITCH_MODE_SYNC: 'int' = 1
    SWITCH_MODE_AT_END: 'int' = 2




class AnimationNodeStateMachineTransition__AdvanceMode(Enum):

    ADVANCE_MODE_DISABLED: 'int' = 0
    ADVANCE_MODE_ENABLED: 'int' = 1
    ADVANCE_MODE_AUTO: 'int' = 2




class AnimationPlayer__AnimationProcessCallback(Enum):

    ANIMATION_PROCESS_PHYSICS: 'int' = 0
    ANIMATION_PROCESS_IDLE: 'int' = 1
    ANIMATION_PROCESS_MANUAL: 'int' = 2




class AnimationPlayer__AnimationMethodCallMode(Enum):

    ANIMATION_METHOD_CALL_DEFERRED: 'int' = 0
    ANIMATION_METHOD_CALL_IMMEDIATE: 'int' = 1




class AnimationTree__AnimationProcessCallback(Enum):

    ANIMATION_PROCESS_PHYSICS: 'int' = 0
    ANIMATION_PROCESS_IDLE: 'int' = 1
    ANIMATION_PROCESS_MANUAL: 'int' = 2




class Area2D__SpaceOverride(Enum):

    SPACE_OVERRIDE_DISABLED: 'int' = 0
    SPACE_OVERRIDE_COMBINE: 'int' = 1
    SPACE_OVERRIDE_COMBINE_REPLACE: 'int' = 2
    SPACE_OVERRIDE_REPLACE: 'int' = 3
    SPACE_OVERRIDE_REPLACE_COMBINE: 'int' = 4




class Area3D__SpaceOverride(Enum):

    SPACE_OVERRIDE_DISABLED: 'int' = 0
    SPACE_OVERRIDE_COMBINE: 'int' = 1
    SPACE_OVERRIDE_COMBINE_REPLACE: 'int' = 2
    SPACE_OVERRIDE_REPLACE: 'int' = 3
    SPACE_OVERRIDE_REPLACE_COMBINE: 'int' = 4




class AspectRatioContainer__StretchMode(Enum):

    STRETCH_WIDTH_CONTROLS_HEIGHT: 'int' = 0
    STRETCH_HEIGHT_CONTROLS_WIDTH: 'int' = 1
    STRETCH_FIT: 'int' = 2
    STRETCH_COVER: 'int' = 3




class AspectRatioContainer__AlignmentMode(Enum):

    ALIGNMENT_BEGIN: 'int' = 0
    ALIGNMENT_CENTER: 'int' = 1
    ALIGNMENT_END: 'int' = 2




class AudioEffectDistortion__Mode(Enum):

    MODE_CLIP: 'int' = 0
    MODE_ATAN: 'int' = 1
    MODE_LOFI: 'int' = 2
    MODE_OVERDRIVE: 'int' = 3
    MODE_WAVESHAPE: 'int' = 4




class AudioEffectFilter__FilterDB(Enum):

    FILTER_6DB: 'int' = 0
    FILTER_12DB: 'int' = 1
    FILTER_18DB: 'int' = 2
    FILTER_24DB: 'int' = 3




class AudioEffectPitchShift__FFTSize(Enum):

    FFT_SIZE_256: 'int' = 0
    FFT_SIZE_512: 'int' = 1
    FFT_SIZE_1024: 'int' = 2
    FFT_SIZE_2048: 'int' = 3
    FFT_SIZE_4096: 'int' = 4
    FFT_SIZE_MAX: 'int' = 5




class AudioEffectSpectrumAnalyzer__FFTSize(Enum):

    FFT_SIZE_256: 'int' = 0
    FFT_SIZE_512: 'int' = 1
    FFT_SIZE_1024: 'int' = 2
    FFT_SIZE_2048: 'int' = 3
    FFT_SIZE_4096: 'int' = 4
    FFT_SIZE_MAX: 'int' = 5




class AudioEffectSpectrumAnalyzerInstance__MagnitudeMode(Enum):

    MAGNITUDE_AVERAGE: 'int' = 0
    MAGNITUDE_MAX: 'int' = 1




class AudioServer__SpeakerMode(Enum):

    SPEAKER_MODE_STEREO: 'int' = 0
    SPEAKER_SURROUND_31: 'int' = 1
    SPEAKER_SURROUND_51: 'int' = 2
    SPEAKER_SURROUND_71: 'int' = 3




class AudioServer__PlaybackType(Enum):

    PLAYBACK_TYPE_DEFAULT: 'int' = 0
    PLAYBACK_TYPE_STREAM: 'int' = 1
    PLAYBACK_TYPE_SAMPLE: 'int' = 2
    PLAYBACK_TYPE_MAX: 'int' = 3




class AudioStreamGenerator__AudioStreamGeneratorMixRate(Enum):

    MIX_RATE_OUTPUT: 'int' = 0
    MIX_RATE_INPUT: 'int' = 1
    MIX_RATE_CUSTOM: 'int' = 2
    MIX_RATE_MAX: 'int' = 3




class AudioStreamInteractive__TransitionFromTime(Enum):

    TRANSITION_FROM_TIME_IMMEDIATE: 'int' = 0
    TRANSITION_FROM_TIME_NEXT_BEAT: 'int' = 1
    TRANSITION_FROM_TIME_NEXT_BAR: 'int' = 2
    TRANSITION_FROM_TIME_END: 'int' = 3




class AudioStreamInteractive__TransitionToTime(Enum):

    TRANSITION_TO_TIME_SAME_POSITION: 'int' = 0
    TRANSITION_TO_TIME_START: 'int' = 1




class AudioStreamInteractive__FadeMode(Enum):

    FADE_DISABLED: 'int' = 0
    FADE_IN: 'int' = 1
    FADE_OUT: 'int' = 2
    FADE_CROSS: 'int' = 3
    FADE_AUTOMATIC: 'int' = 4




class AudioStreamInteractive__AutoAdvanceMode(Enum):

    AUTO_ADVANCE_DISABLED: 'int' = 0
    AUTO_ADVANCE_ENABLED: 'int' = 1
    AUTO_ADVANCE_RETURN_TO_HOLD: 'int' = 2




class AudioStreamPlayer__MixTarget(Enum):

    MIX_TARGET_STEREO: 'int' = 0
    MIX_TARGET_SURROUND: 'int' = 1
    MIX_TARGET_CENTER: 'int' = 2




class AudioStreamPlayer3D__AttenuationModel(Enum):

    ATTENUATION_INVERSE_DISTANCE: 'int' = 0
    ATTENUATION_INVERSE_SQUARE_DISTANCE: 'int' = 1
    ATTENUATION_LOGARITHMIC: 'int' = 2
    ATTENUATION_DISABLED: 'int' = 3




class AudioStreamPlayer3D__DopplerTracking(Enum):

    DOPPLER_TRACKING_DISABLED: 'int' = 0
    DOPPLER_TRACKING_IDLE_STEP: 'int' = 1
    DOPPLER_TRACKING_PHYSICS_STEP: 'int' = 2




class AudioStreamRandomizer__PlaybackMode(Enum):

    PLAYBACK_RANDOM_NO_REPEATS: 'int' = 0
    PLAYBACK_RANDOM: 'int' = 1
    PLAYBACK_SEQUENTIAL: 'int' = 2




class AudioStreamWAV__Format(Enum):

    FORMAT_8_BITS: 'int' = 0
    FORMAT_16_BITS: 'int' = 1
    FORMAT_IMA_ADPCM: 'int' = 2
    FORMAT_QOA: 'int' = 3




class AudioStreamWAV__LoopMode(Enum):

    LOOP_DISABLED: 'int' = 0
    LOOP_FORWARD: 'int' = 1
    LOOP_PINGPONG: 'int' = 2
    LOOP_BACKWARD: 'int' = 3




class BackBufferCopy__CopyMode(Enum):

    COPY_MODE_DISABLED: 'int' = 0
    COPY_MODE_RECT: 'int' = 1
    COPY_MODE_VIEWPORT: 'int' = 2




class BaseButton__DrawMode(Enum):

    DRAW_NORMAL: 'int' = 0
    DRAW_PRESSED: 'int' = 1
    DRAW_HOVER: 'int' = 2
    DRAW_DISABLED: 'int' = 3
    DRAW_HOVER_PRESSED: 'int' = 4




class BaseButton__ActionMode(Enum):

    ACTION_MODE_BUTTON_PRESS: 'int' = 0
    ACTION_MODE_BUTTON_RELEASE: 'int' = 1




class BaseMaterial3D__TextureParam(Enum):

    TEXTURE_ALBEDO: 'int' = 0
    TEXTURE_METALLIC: 'int' = 1
    TEXTURE_ROUGHNESS: 'int' = 2
    TEXTURE_EMISSION: 'int' = 3
    TEXTURE_NORMAL: 'int' = 4
    TEXTURE_RIM: 'int' = 5
    TEXTURE_CLEARCOAT: 'int' = 6
    TEXTURE_FLOWMAP: 'int' = 7
    TEXTURE_AMBIENT_OCCLUSION: 'int' = 8
    TEXTURE_HEIGHTMAP: 'int' = 9
    TEXTURE_SUBSURFACE_SCATTERING: 'int' = 10
    TEXTURE_SUBSURFACE_TRANSMITTANCE: 'int' = 11
    TEXTURE_BACKLIGHT: 'int' = 12
    TEXTURE_REFRACTION: 'int' = 13
    TEXTURE_DETAIL_MASK: 'int' = 14
    TEXTURE_DETAIL_ALBEDO: 'int' = 15
    TEXTURE_DETAIL_NORMAL: 'int' = 16
    TEXTURE_ORM: 'int' = 17
    TEXTURE_MAX: 'int' = 18




class BaseMaterial3D__TextureFilter(Enum):

    TEXTURE_FILTER_NEAREST: 'int' = 0
    TEXTURE_FILTER_LINEAR: 'int' = 1
    TEXTURE_FILTER_NEAREST_WITH_MIPMAPS: 'int' = 2
    TEXTURE_FILTER_LINEAR_WITH_MIPMAPS: 'int' = 3
    TEXTURE_FILTER_NEAREST_WITH_MIPMAPS_ANISOTROPIC: 'int' = 4
    TEXTURE_FILTER_LINEAR_WITH_MIPMAPS_ANISOTROPIC: 'int' = 5
    TEXTURE_FILTER_MAX: 'int' = 6




class BaseMaterial3D__DetailUV(Enum):

    DETAIL_UV_1: 'int' = 0
    DETAIL_UV_2: 'int' = 1




class BaseMaterial3D__Transparency(Enum):

    TRANSPARENCY_DISABLED: 'int' = 0
    TRANSPARENCY_ALPHA: 'int' = 1
    TRANSPARENCY_ALPHA_SCISSOR: 'int' = 2
    TRANSPARENCY_ALPHA_HASH: 'int' = 3
    TRANSPARENCY_ALPHA_DEPTH_PRE_PASS: 'int' = 4
    TRANSPARENCY_MAX: 'int' = 5




class BaseMaterial3D__ShadingMode(Enum):

    SHADING_MODE_UNSHADED: 'int' = 0
    SHADING_MODE_PER_PIXEL: 'int' = 1
    SHADING_MODE_PER_VERTEX: 'int' = 2
    SHADING_MODE_MAX: 'int' = 3




class BaseMaterial3D__Feature(Enum):

    FEATURE_EMISSION: 'int' = 0
    FEATURE_NORMAL_MAPPING: 'int' = 1
    FEATURE_RIM: 'int' = 2
    FEATURE_CLEARCOAT: 'int' = 3
    FEATURE_ANISOTROPY: 'int' = 4
    FEATURE_AMBIENT_OCCLUSION: 'int' = 5
    FEATURE_HEIGHT_MAPPING: 'int' = 6
    FEATURE_SUBSURFACE_SCATTERING: 'int' = 7
    FEATURE_SUBSURFACE_TRANSMITTANCE: 'int' = 8
    FEATURE_BACKLIGHT: 'int' = 9
    FEATURE_REFRACTION: 'int' = 10
    FEATURE_DETAIL: 'int' = 11
    FEATURE_MAX: 'int' = 12




class BaseMaterial3D__BlendMode(Enum):

    BLEND_MODE_MIX: 'int' = 0
    BLEND_MODE_ADD: 'int' = 1
    BLEND_MODE_SUB: 'int' = 2
    BLEND_MODE_MUL: 'int' = 3
    BLEND_MODE_PREMULT_ALPHA: 'int' = 4




class BaseMaterial3D__AlphaAntiAliasing(Enum):

    ALPHA_ANTIALIASING_OFF: 'int' = 0
    ALPHA_ANTIALIASING_ALPHA_TO_COVERAGE: 'int' = 1
    ALPHA_ANTIALIASING_ALPHA_TO_COVERAGE_AND_TO_ONE: 'int' = 2




class BaseMaterial3D__DepthDrawMode(Enum):

    DEPTH_DRAW_OPAQUE_ONLY: 'int' = 0
    DEPTH_DRAW_ALWAYS: 'int' = 1
    DEPTH_DRAW_DISABLED: 'int' = 2




class BaseMaterial3D__CullMode(Enum):

    CULL_BACK: 'int' = 0
    CULL_FRONT: 'int' = 1
    CULL_DISABLED: 'int' = 2




class BaseMaterial3D__Flags(Enum):

    FLAG_DISABLE_DEPTH_TEST: 'int' = 0
    FLAG_ALBEDO_FROM_VERTEX_COLOR: 'int' = 1
    FLAG_SRGB_VERTEX_COLOR: 'int' = 2
    FLAG_USE_POINT_SIZE: 'int' = 3
    FLAG_FIXED_SIZE: 'int' = 4
    FLAG_BILLBOARD_KEEP_SCALE: 'int' = 5
    FLAG_UV1_USE_TRIPLANAR: 'int' = 6
    FLAG_UV2_USE_TRIPLANAR: 'int' = 7
    FLAG_UV1_USE_WORLD_TRIPLANAR: 'int' = 8
    FLAG_UV2_USE_WORLD_TRIPLANAR: 'int' = 9
    FLAG_AO_ON_UV2: 'int' = 10
    FLAG_EMISSION_ON_UV2: 'int' = 11
    FLAG_ALBEDO_TEXTURE_FORCE_SRGB: 'int' = 12
    FLAG_DONT_RECEIVE_SHADOWS: 'int' = 13
    FLAG_DISABLE_AMBIENT_LIGHT: 'int' = 14
    FLAG_USE_SHADOW_TO_OPACITY: 'int' = 15
    FLAG_USE_TEXTURE_REPEAT: 'int' = 16
    FLAG_INVERT_HEIGHTMAP: 'int' = 17
    FLAG_SUBSURFACE_MODE_SKIN: 'int' = 18
    FLAG_PARTICLE_TRAILS_MODE: 'int' = 19
    FLAG_ALBEDO_TEXTURE_MSDF: 'int' = 20
    FLAG_DISABLE_FOG: 'int' = 21
    FLAG_MAX: 'int' = 22




class BaseMaterial3D__DiffuseMode(Enum):

    DIFFUSE_BURLEY: 'int' = 0
    DIFFUSE_LAMBERT: 'int' = 1
    DIFFUSE_LAMBERT_WRAP: 'int' = 2
    DIFFUSE_TOON: 'int' = 3




class BaseMaterial3D__SpecularMode(Enum):

    SPECULAR_SCHLICK_GGX: 'int' = 0
    SPECULAR_TOON: 'int' = 1
    SPECULAR_DISABLED: 'int' = 2




class BaseMaterial3D__BillboardMode(Enum):

    BILLBOARD_DISABLED: 'int' = 0
    BILLBOARD_ENABLED: 'int' = 1
    BILLBOARD_FIXED_Y: 'int' = 2
    BILLBOARD_PARTICLES: 'int' = 3




class BaseMaterial3D__TextureChannel(Enum):

    TEXTURE_CHANNEL_RED: 'int' = 0
    TEXTURE_CHANNEL_GREEN: 'int' = 1
    TEXTURE_CHANNEL_BLUE: 'int' = 2
    TEXTURE_CHANNEL_ALPHA: 'int' = 3
    TEXTURE_CHANNEL_GRAYSCALE: 'int' = 4




class BaseMaterial3D__EmissionOperator(Enum):

    EMISSION_OP_ADD: 'int' = 0
    EMISSION_OP_MULTIPLY: 'int' = 1




class BaseMaterial3D__DistanceFadeMode(Enum):

    DISTANCE_FADE_DISABLED: 'int' = 0
    DISTANCE_FADE_PIXEL_ALPHA: 'int' = 1
    DISTANCE_FADE_PIXEL_DITHER: 'int' = 2
    DISTANCE_FADE_OBJECT_DITHER: 'int' = 3




class BoxContainer__AlignmentMode(Enum):

    ALIGNMENT_BEGIN: 'int' = 0
    ALIGNMENT_CENTER: 'int' = 1
    ALIGNMENT_END: 'int' = 2




class CPUParticles2D__DrawOrder(Enum):

    DRAW_ORDER_INDEX: 'int' = 0
    DRAW_ORDER_LIFETIME: 'int' = 1




class CPUParticles2D__Parameter(Enum):

    PARAM_INITIAL_LINEAR_VELOCITY: 'int' = 0
    PARAM_ANGULAR_VELOCITY: 'int' = 1
    PARAM_ORBIT_VELOCITY: 'int' = 2
    PARAM_LINEAR_ACCEL: 'int' = 3
    PARAM_RADIAL_ACCEL: 'int' = 4
    PARAM_TANGENTIAL_ACCEL: 'int' = 5
    PARAM_DAMPING: 'int' = 6
    PARAM_ANGLE: 'int' = 7
    PARAM_SCALE: 'int' = 8
    PARAM_HUE_VARIATION: 'int' = 9
    PARAM_ANIM_SPEED: 'int' = 10
    PARAM_ANIM_OFFSET: 'int' = 11
    PARAM_MAX: 'int' = 12




class CPUParticles2D__ParticleFlags(Enum):

    PARTICLE_FLAG_ALIGN_Y_TO_VELOCITY: 'int' = 0
    PARTICLE_FLAG_ROTATE_Y: 'int' = 1
    PARTICLE_FLAG_DISABLE_Z: 'int' = 2
    PARTICLE_FLAG_MAX: 'int' = 3




class CPUParticles2D__EmissionShape(Enum):

    EMISSION_SHAPE_POINT: 'int' = 0
    EMISSION_SHAPE_SPHERE: 'int' = 1
    EMISSION_SHAPE_SPHERE_SURFACE: 'int' = 2
    EMISSION_SHAPE_RECTANGLE: 'int' = 3
    EMISSION_SHAPE_POINTS: 'int' = 4
    EMISSION_SHAPE_DIRECTED_POINTS: 'int' = 5
    EMISSION_SHAPE_MAX: 'int' = 6




class CPUParticles3D__DrawOrder(Enum):

    DRAW_ORDER_INDEX: 'int' = 0
    DRAW_ORDER_LIFETIME: 'int' = 1
    DRAW_ORDER_VIEW_DEPTH: 'int' = 2




class CPUParticles3D__Parameter(Enum):

    PARAM_INITIAL_LINEAR_VELOCITY: 'int' = 0
    PARAM_ANGULAR_VELOCITY: 'int' = 1
    PARAM_ORBIT_VELOCITY: 'int' = 2
    PARAM_LINEAR_ACCEL: 'int' = 3
    PARAM_RADIAL_ACCEL: 'int' = 4
    PARAM_TANGENTIAL_ACCEL: 'int' = 5
    PARAM_DAMPING: 'int' = 6
    PARAM_ANGLE: 'int' = 7
    PARAM_SCALE: 'int' = 8
    PARAM_HUE_VARIATION: 'int' = 9
    PARAM_ANIM_SPEED: 'int' = 10
    PARAM_ANIM_OFFSET: 'int' = 11
    PARAM_MAX: 'int' = 12




class CPUParticles3D__ParticleFlags(Enum):

    PARTICLE_FLAG_ALIGN_Y_TO_VELOCITY: 'int' = 0
    PARTICLE_FLAG_ROTATE_Y: 'int' = 1
    PARTICLE_FLAG_DISABLE_Z: 'int' = 2
    PARTICLE_FLAG_MAX: 'int' = 3




class CPUParticles3D__EmissionShape(Enum):

    EMISSION_SHAPE_POINT: 'int' = 0
    EMISSION_SHAPE_SPHERE: 'int' = 1
    EMISSION_SHAPE_SPHERE_SURFACE: 'int' = 2
    EMISSION_SHAPE_BOX: 'int' = 3
    EMISSION_SHAPE_POINTS: 'int' = 4
    EMISSION_SHAPE_DIRECTED_POINTS: 'int' = 5
    EMISSION_SHAPE_RING: 'int' = 6
    EMISSION_SHAPE_MAX: 'int' = 7




class CSGPolygon3D__Mode(Enum):

    MODE_DEPTH: 'int' = 0
    MODE_SPIN: 'int' = 1
    MODE_PATH: 'int' = 2




class CSGPolygon3D__PathRotation(Enum):

    PATH_ROTATION_POLYGON: 'int' = 0
    PATH_ROTATION_PATH: 'int' = 1
    PATH_ROTATION_PATH_FOLLOW: 'int' = 2




class CSGPolygon3D__PathIntervalType(Enum):

    PATH_INTERVAL_DISTANCE: 'int' = 0
    PATH_INTERVAL_SUBDIVIDE: 'int' = 1




class CSGShape3D__Operation(Enum):

    OPERATION_UNION: 'int' = 0
    OPERATION_INTERSECTION: 'int' = 1
    OPERATION_SUBTRACTION: 'int' = 2




class Camera2D__AnchorMode(Enum):

    ANCHOR_MODE_FIXED_TOP_LEFT: 'int' = 0
    ANCHOR_MODE_DRAG_CENTER: 'int' = 1




class Camera2D__Camera2DProcessCallback(Enum):

    CAMERA2D_PROCESS_PHYSICS: 'int' = 0
    CAMERA2D_PROCESS_IDLE: 'int' = 1




class Camera3D__ProjectionType(Enum):

    PROJECTION_PERSPECTIVE: 'int' = 0
    PROJECTION_ORTHOGONAL: 'int' = 1
    PROJECTION_FRUSTUM: 'int' = 2




class Camera3D__KeepAspect(Enum):

    KEEP_WIDTH: 'int' = 0
    KEEP_HEIGHT: 'int' = 1




class Camera3D__DopplerTracking(Enum):

    DOPPLER_TRACKING_DISABLED: 'int' = 0
    DOPPLER_TRACKING_IDLE_STEP: 'int' = 1
    DOPPLER_TRACKING_PHYSICS_STEP: 'int' = 2




class CameraFeed__FeedDataType(Enum):

    FEED_NOIMAGE: 'int' = 0
    FEED_RGB: 'int' = 1
    FEED_YCBCR: 'int' = 2
    FEED_YCBCR_SEP: 'int' = 3
    FEED_EXTERNAL: 'int' = 4




class CameraFeed__FeedPosition(Enum):

    FEED_UNSPECIFIED: 'int' = 0
    FEED_FRONT: 'int' = 1
    FEED_BACK: 'int' = 2




class CameraServer__FeedImage(Enum):

    FEED_RGBA_IMAGE: 'int' = 0
    FEED_YCBCR_IMAGE: 'int' = 0
    FEED_Y_IMAGE: 'int' = 0
    FEED_CBCR_IMAGE: 'int' = 1




class CanvasItem__TextureFilter(Enum):

    TEXTURE_FILTER_PARENT_NODE: 'int' = 0
    TEXTURE_FILTER_NEAREST: 'int' = 1
    TEXTURE_FILTER_LINEAR: 'int' = 2
    TEXTURE_FILTER_NEAREST_WITH_MIPMAPS: 'int' = 3
    TEXTURE_FILTER_LINEAR_WITH_MIPMAPS: 'int' = 4
    TEXTURE_FILTER_NEAREST_WITH_MIPMAPS_ANISOTROPIC: 'int' = 5
    TEXTURE_FILTER_LINEAR_WITH_MIPMAPS_ANISOTROPIC: 'int' = 6
    TEXTURE_FILTER_MAX: 'int' = 7




class CanvasItem__TextureRepeat(Enum):

    TEXTURE_REPEAT_PARENT_NODE: 'int' = 0
    TEXTURE_REPEAT_DISABLED: 'int' = 1
    TEXTURE_REPEAT_ENABLED: 'int' = 2
    TEXTURE_REPEAT_MIRROR: 'int' = 3
    TEXTURE_REPEAT_MAX: 'int' = 4




class CanvasItem__ClipChildrenMode(Enum):

    CLIP_CHILDREN_DISABLED: 'int' = 0
    CLIP_CHILDREN_ONLY: 'int' = 1
    CLIP_CHILDREN_AND_DRAW: 'int' = 2
    CLIP_CHILDREN_MAX: 'int' = 3




class CanvasItemMaterial__BlendMode(Enum):

    BLEND_MODE_MIX: 'int' = 0
    BLEND_MODE_ADD: 'int' = 1
    BLEND_MODE_SUB: 'int' = 2
    BLEND_MODE_MUL: 'int' = 3
    BLEND_MODE_PREMULT_ALPHA: 'int' = 4




class CanvasItemMaterial__LightMode(Enum):

    LIGHT_MODE_NORMAL: 'int' = 0
    LIGHT_MODE_UNSHADED: 'int' = 1
    LIGHT_MODE_LIGHT_ONLY: 'int' = 2




class CharacterBody2D__MotionMode(Enum):

    MOTION_MODE_GROUNDED: 'int' = 0
    MOTION_MODE_FLOATING: 'int' = 1




class CharacterBody2D__PlatformOnLeave(Enum):

    PLATFORM_ON_LEAVE_ADD_VELOCITY: 'int' = 0
    PLATFORM_ON_LEAVE_ADD_UPWARD_VELOCITY: 'int' = 1
    PLATFORM_ON_LEAVE_DO_NOTHING: 'int' = 2




class CharacterBody3D__MotionMode(Enum):

    MOTION_MODE_GROUNDED: 'int' = 0
    MOTION_MODE_FLOATING: 'int' = 1




class CharacterBody3D__PlatformOnLeave(Enum):

    PLATFORM_ON_LEAVE_ADD_VELOCITY: 'int' = 0
    PLATFORM_ON_LEAVE_ADD_UPWARD_VELOCITY: 'int' = 1
    PLATFORM_ON_LEAVE_DO_NOTHING: 'int' = 2




class ClassDB__APIType(Enum):

    API_CORE: 'int' = 0
    API_EDITOR: 'int' = 1
    API_EXTENSION: 'int' = 2
    API_EDITOR_EXTENSION: 'int' = 3
    API_NONE: 'int' = 4




class CodeEdit__CodeCompletionKind(Enum):

    KIND_CLASS: 'int' = 0
    KIND_FUNCTION: 'int' = 1
    KIND_SIGNAL: 'int' = 2
    KIND_VARIABLE: 'int' = 3
    KIND_MEMBER: 'int' = 4
    KIND_ENUM: 'int' = 5
    KIND_CONSTANT: 'int' = 6
    KIND_NODE_PATH: 'int' = 7
    KIND_FILE_PATH: 'int' = 8
    KIND_PLAIN_TEXT: 'int' = 9




class CodeEdit__CodeCompletionLocation(Enum):

    LOCATION_LOCAL: 'int' = 0
    LOCATION_PARENT_MASK: 'int' = 256
    LOCATION_OTHER_USER_CODE: 'int' = 512
    LOCATION_OTHER: 'int' = 1024




class CollisionObject2D__DisableMode(Enum):

    DISABLE_MODE_REMOVE: 'int' = 0
    DISABLE_MODE_MAKE_STATIC: 'int' = 1
    DISABLE_MODE_KEEP_ACTIVE: 'int' = 2




class CollisionObject3D__DisableMode(Enum):

    DISABLE_MODE_REMOVE: 'int' = 0
    DISABLE_MODE_MAKE_STATIC: 'int' = 1
    DISABLE_MODE_KEEP_ACTIVE: 'int' = 2




class CollisionPolygon2D__BuildMode(Enum):

    BUILD_SOLIDS: 'int' = 0
    BUILD_SEGMENTS: 'int' = 1




class ColorPicker__ColorModeType(Enum):

    MODE_RGB: 'int' = 0
    MODE_HSV: 'int' = 1
    MODE_RAW: 'int' = 2
    MODE_OKHSL: 'int' = 3




class ColorPicker__PickerShapeType(Enum):

    SHAPE_HSV_RECTANGLE: 'int' = 0
    SHAPE_HSV_WHEEL: 'int' = 1
    SHAPE_VHS_CIRCLE: 'int' = 2
    SHAPE_OKHSL_CIRCLE: 'int' = 3
    SHAPE_NONE: 'int' = 4




class CompositorEffect__EffectCallbackType(Enum):

    EFFECT_CALLBACK_TYPE_PRE_OPAQUE: 'int' = 0
    EFFECT_CALLBACK_TYPE_POST_OPAQUE: 'int' = 1
    EFFECT_CALLBACK_TYPE_POST_SKY: 'int' = 2
    EFFECT_CALLBACK_TYPE_PRE_TRANSPARENT: 'int' = 3
    EFFECT_CALLBACK_TYPE_POST_TRANSPARENT: 'int' = 4
    EFFECT_CALLBACK_TYPE_MAX: 'int' = 5




class ConeTwistJoint3D__Param(Enum):

    PARAM_SWING_SPAN: 'int' = 0
    PARAM_TWIST_SPAN: 'int' = 1
    PARAM_BIAS: 'int' = 2
    PARAM_SOFTNESS: 'int' = 3
    PARAM_RELAXATION: 'int' = 4
    PARAM_MAX: 'int' = 5




class Control__FocusMode(Enum):

    FOCUS_NONE: 'int' = 0
    FOCUS_CLICK: 'int' = 1
    FOCUS_ALL: 'int' = 2




class Control__CursorShape(Enum):

    CURSOR_ARROW: 'int' = 0
    CURSOR_IBEAM: 'int' = 1
    CURSOR_POINTING_HAND: 'int' = 2
    CURSOR_CROSS: 'int' = 3
    CURSOR_WAIT: 'int' = 4
    CURSOR_BUSY: 'int' = 5
    CURSOR_DRAG: 'int' = 6
    CURSOR_CAN_DROP: 'int' = 7
    CURSOR_FORBIDDEN: 'int' = 8
    CURSOR_VSIZE: 'int' = 9
    CURSOR_HSIZE: 'int' = 10
    CURSOR_BDIAGSIZE: 'int' = 11
    CURSOR_FDIAGSIZE: 'int' = 12
    CURSOR_MOVE: 'int' = 13
    CURSOR_VSPLIT: 'int' = 14
    CURSOR_HSPLIT: 'int' = 15
    CURSOR_HELP: 'int' = 16




class Control__LayoutPreset(Enum):

    PRESET_TOP_LEFT: 'int' = 0
    PRESET_TOP_RIGHT: 'int' = 1
    PRESET_BOTTOM_LEFT: 'int' = 2
    PRESET_BOTTOM_RIGHT: 'int' = 3
    PRESET_CENTER_LEFT: 'int' = 4
    PRESET_CENTER_TOP: 'int' = 5
    PRESET_CENTER_RIGHT: 'int' = 6
    PRESET_CENTER_BOTTOM: 'int' = 7
    PRESET_CENTER: 'int' = 8
    PRESET_LEFT_WIDE: 'int' = 9
    PRESET_TOP_WIDE: 'int' = 10
    PRESET_RIGHT_WIDE: 'int' = 11
    PRESET_BOTTOM_WIDE: 'int' = 12
    PRESET_VCENTER_WIDE: 'int' = 13
    PRESET_HCENTER_WIDE: 'int' = 14
    PRESET_FULL_RECT: 'int' = 15




class Control__LayoutPresetMode(Enum):

    PRESET_MODE_MINSIZE: 'int' = 0
    PRESET_MODE_KEEP_WIDTH: 'int' = 1
    PRESET_MODE_KEEP_HEIGHT: 'int' = 2
    PRESET_MODE_KEEP_SIZE: 'int' = 3




class Control__SizeFlags(Enum):

    SIZE_SHRINK_BEGIN: 'int' = 0
    SIZE_FILL: 'int' = 1
    SIZE_EXPAND: 'int' = 2
    SIZE_EXPAND_FILL: 'int' = 3
    SIZE_SHRINK_CENTER: 'int' = 4
    SIZE_SHRINK_END: 'int' = 8




class Control__MouseFilter(Enum):

    MOUSE_FILTER_STOP: 'int' = 0
    MOUSE_FILTER_PASS: 'int' = 1
    MOUSE_FILTER_IGNORE: 'int' = 2




class Control__GrowDirection(Enum):

    GROW_DIRECTION_BEGIN: 'int' = 0
    GROW_DIRECTION_END: 'int' = 1
    GROW_DIRECTION_BOTH: 'int' = 2




class Control__Anchor(Enum):

    ANCHOR_BEGIN: 'int' = 0
    ANCHOR_END: 'int' = 1




class Control__LayoutDirection(Enum):

    LAYOUT_DIRECTION_INHERITED: 'int' = 0
    LAYOUT_DIRECTION_APPLICATION_LOCALE: 'int' = 1
    LAYOUT_DIRECTION_LTR: 'int' = 2
    LAYOUT_DIRECTION_RTL: 'int' = 3
    LAYOUT_DIRECTION_SYSTEM_LOCALE: 'int' = 4
    LAYOUT_DIRECTION_MAX: 'int' = 5
    LAYOUT_DIRECTION_LOCALE: 'int' = 1




class Control__TextDirection(Enum):

    TEXT_DIRECTION_INHERITED: 'int' = 3
    TEXT_DIRECTION_AUTO: 'int' = 0
    TEXT_DIRECTION_LTR: 'int' = 1
    TEXT_DIRECTION_RTL: 'int' = 2




class Curve__TangentMode(Enum):

    TANGENT_FREE: 'int' = 0
    TANGENT_LINEAR: 'int' = 1
    TANGENT_MODE_COUNT: 'int' = 2




class CurveTexture__TextureMode(Enum):

    TEXTURE_MODE_RGB: 'int' = 0
    TEXTURE_MODE_RED: 'int' = 1




class Decal__DecalTexture(Enum):

    TEXTURE_ALBEDO: 'int' = 0
    TEXTURE_NORMAL: 'int' = 1
    TEXTURE_ORM: 'int' = 2
    TEXTURE_EMISSION: 'int' = 3
    TEXTURE_MAX: 'int' = 4




class DirectionalLight3D__ShadowMode(Enum):

    SHADOW_ORTHOGONAL: 'int' = 0
    SHADOW_PARALLEL_2_SPLITS: 'int' = 1
    SHADOW_PARALLEL_4_SPLITS: 'int' = 2




class DirectionalLight3D__SkyMode(Enum):

    SKY_MODE_LIGHT_AND_SKY: 'int' = 0
    SKY_MODE_LIGHT_ONLY: 'int' = 1
    SKY_MODE_SKY_ONLY: 'int' = 2




class DisplayServer__Feature(Enum):

    FEATURE_GLOBAL_MENU: 'int' = 0
    FEATURE_SUBWINDOWS: 'int' = 1
    FEATURE_TOUCHSCREEN: 'int' = 2
    FEATURE_MOUSE: 'int' = 3
    FEATURE_MOUSE_WARP: 'int' = 4
    FEATURE_CLIPBOARD: 'int' = 5
    FEATURE_VIRTUAL_KEYBOARD: 'int' = 6
    FEATURE_CURSOR_SHAPE: 'int' = 7
    FEATURE_CUSTOM_CURSOR_SHAPE: 'int' = 8
    FEATURE_NATIVE_DIALOG: 'int' = 9
    FEATURE_IME: 'int' = 10
    FEATURE_WINDOW_TRANSPARENCY: 'int' = 11
    FEATURE_HIDPI: 'int' = 12
    FEATURE_ICON: 'int' = 13
    FEATURE_NATIVE_ICON: 'int' = 14
    FEATURE_ORIENTATION: 'int' = 15
    FEATURE_SWAP_BUFFERS: 'int' = 16
    FEATURE_CLIPBOARD_PRIMARY: 'int' = 18
    FEATURE_TEXT_TO_SPEECH: 'int' = 19
    FEATURE_EXTEND_TO_TITLE: 'int' = 20
    FEATURE_SCREEN_CAPTURE: 'int' = 21
    FEATURE_STATUS_INDICATOR: 'int' = 22
    FEATURE_NATIVE_HELP: 'int' = 23
    FEATURE_NATIVE_DIALOG_INPUT: 'int' = 24
    FEATURE_NATIVE_DIALOG_FILE: 'int' = 25
    FEATURE_NATIVE_DIALOG_FILE_EXTRA: 'int' = 26
    FEATURE_WINDOW_DRAG: 'int' = 27
    FEATURE_SCREEN_EXCLUDE_FROM_CAPTURE: 'int' = 28
    FEATURE_WINDOW_EMBEDDING: 'int' = 29
    FEATURE_NATIVE_DIALOG_FILE_MIME: 'int' = 30
    FEATURE_EMOJI_AND_SYMBOL_PICKER: 'int' = 31




class DisplayServer__MouseMode(Enum):

    MOUSE_MODE_VISIBLE: 'int' = 0
    MOUSE_MODE_HIDDEN: 'int' = 1
    MOUSE_MODE_CAPTURED: 'int' = 2
    MOUSE_MODE_CONFINED: 'int' = 3
    MOUSE_MODE_CONFINED_HIDDEN: 'int' = 4
    MOUSE_MODE_MAX: 'int' = 5




class DisplayServer__ScreenOrientation(Enum):

    SCREEN_LANDSCAPE: 'int' = 0
    SCREEN_PORTRAIT: 'int' = 1
    SCREEN_REVERSE_LANDSCAPE: 'int' = 2
    SCREEN_REVERSE_PORTRAIT: 'int' = 3
    SCREEN_SENSOR_LANDSCAPE: 'int' = 4
    SCREEN_SENSOR_PORTRAIT: 'int' = 5
    SCREEN_SENSOR: 'int' = 6




class DisplayServer__VirtualKeyboardType(Enum):

    KEYBOARD_TYPE_DEFAULT: 'int' = 0
    KEYBOARD_TYPE_MULTILINE: 'int' = 1
    KEYBOARD_TYPE_NUMBER: 'int' = 2
    KEYBOARD_TYPE_NUMBER_DECIMAL: 'int' = 3
    KEYBOARD_TYPE_PHONE: 'int' = 4
    KEYBOARD_TYPE_EMAIL_ADDRESS: 'int' = 5
    KEYBOARD_TYPE_PASSWORD: 'int' = 6
    KEYBOARD_TYPE_URL: 'int' = 7




class DisplayServer__CursorShape(Enum):

    CURSOR_ARROW: 'int' = 0
    CURSOR_IBEAM: 'int' = 1
    CURSOR_POINTING_HAND: 'int' = 2
    CURSOR_CROSS: 'int' = 3
    CURSOR_WAIT: 'int' = 4
    CURSOR_BUSY: 'int' = 5
    CURSOR_DRAG: 'int' = 6
    CURSOR_CAN_DROP: 'int' = 7
    CURSOR_FORBIDDEN: 'int' = 8
    CURSOR_VSIZE: 'int' = 9
    CURSOR_HSIZE: 'int' = 10
    CURSOR_BDIAGSIZE: 'int' = 11
    CURSOR_FDIAGSIZE: 'int' = 12
    CURSOR_MOVE: 'int' = 13
    CURSOR_VSPLIT: 'int' = 14
    CURSOR_HSPLIT: 'int' = 15
    CURSOR_HELP: 'int' = 16
    CURSOR_MAX: 'int' = 17




class DisplayServer__FileDialogMode(Enum):

    FILE_DIALOG_MODE_OPEN_FILE: 'int' = 0
    FILE_DIALOG_MODE_OPEN_FILES: 'int' = 1
    FILE_DIALOG_MODE_OPEN_DIR: 'int' = 2
    FILE_DIALOG_MODE_OPEN_ANY: 'int' = 3
    FILE_DIALOG_MODE_SAVE_FILE: 'int' = 4




class DisplayServer__WindowMode(Enum):

    WINDOW_MODE_WINDOWED: 'int' = 0
    WINDOW_MODE_MINIMIZED: 'int' = 1
    WINDOW_MODE_MAXIMIZED: 'int' = 2
    WINDOW_MODE_FULLSCREEN: 'int' = 3
    WINDOW_MODE_EXCLUSIVE_FULLSCREEN: 'int' = 4




class DisplayServer__WindowFlags(Enum):

    WINDOW_FLAG_RESIZE_DISABLED: 'int' = 0
    WINDOW_FLAG_BORDERLESS: 'int' = 1
    WINDOW_FLAG_ALWAYS_ON_TOP: 'int' = 2
    WINDOW_FLAG_TRANSPARENT: 'int' = 3
    WINDOW_FLAG_NO_FOCUS: 'int' = 4
    WINDOW_FLAG_POPUP: 'int' = 5
    WINDOW_FLAG_EXTEND_TO_TITLE: 'int' = 6
    WINDOW_FLAG_MOUSE_PASSTHROUGH: 'int' = 7
    WINDOW_FLAG_SHARP_CORNERS: 'int' = 8
    WINDOW_FLAG_EXCLUDE_FROM_CAPTURE: 'int' = 9
    WINDOW_FLAG_MAX: 'int' = 10




class DisplayServer__WindowEvent(Enum):

    WINDOW_EVENT_MOUSE_ENTER: 'int' = 0
    WINDOW_EVENT_MOUSE_EXIT: 'int' = 1
    WINDOW_EVENT_FOCUS_IN: 'int' = 2
    WINDOW_EVENT_FOCUS_OUT: 'int' = 3
    WINDOW_EVENT_CLOSE_REQUEST: 'int' = 4
    WINDOW_EVENT_GO_BACK_REQUEST: 'int' = 5
    WINDOW_EVENT_DPI_CHANGE: 'int' = 6
    WINDOW_EVENT_TITLEBAR_CHANGE: 'int' = 7




class DisplayServer__WindowResizeEdge(Enum):

    WINDOW_EDGE_TOP_LEFT: 'int' = 0
    WINDOW_EDGE_TOP: 'int' = 1
    WINDOW_EDGE_TOP_RIGHT: 'int' = 2
    WINDOW_EDGE_LEFT: 'int' = 3
    WINDOW_EDGE_RIGHT: 'int' = 4
    WINDOW_EDGE_BOTTOM_LEFT: 'int' = 5
    WINDOW_EDGE_BOTTOM: 'int' = 6
    WINDOW_EDGE_BOTTOM_RIGHT: 'int' = 7
    WINDOW_EDGE_MAX: 'int' = 8




class DisplayServer__VSyncMode(Enum):

    VSYNC_DISABLED: 'int' = 0
    VSYNC_ENABLED: 'int' = 1
    VSYNC_ADAPTIVE: 'int' = 2
    VSYNC_MAILBOX: 'int' = 3




class DisplayServer__HandleType(Enum):

    DISPLAY_HANDLE: 'int' = 0
    WINDOW_HANDLE: 'int' = 1
    WINDOW_VIEW: 'int' = 2
    OPENGL_CONTEXT: 'int' = 3
    EGL_DISPLAY: 'int' = 4
    EGL_CONFIG: 'int' = 5




class DisplayServer__TTSUtteranceEvent(Enum):

    TTS_UTTERANCE_STARTED: 'int' = 0
    TTS_UTTERANCE_ENDED: 'int' = 1
    TTS_UTTERANCE_CANCELED: 'int' = 2
    TTS_UTTERANCE_BOUNDARY: 'int' = 3




class ENetConnection__CompressionMode(Enum):

    COMPRESS_NONE: 'int' = 0
    COMPRESS_RANGE_CODER: 'int' = 1
    COMPRESS_FASTLZ: 'int' = 2
    COMPRESS_ZLIB: 'int' = 3
    COMPRESS_ZSTD: 'int' = 4




class ENetConnection__EventType(Enum):

    EVENT_ERROR: 'int' = -1
    EVENT_NONE: 'int' = 0
    EVENT_CONNECT: 'int' = 1
    EVENT_DISCONNECT: 'int' = 2
    EVENT_RECEIVE: 'int' = 3




class ENetConnection__HostStatistic(Enum):

    HOST_TOTAL_SENT_DATA: 'int' = 0
    HOST_TOTAL_SENT_PACKETS: 'int' = 1
    HOST_TOTAL_RECEIVED_DATA: 'int' = 2
    HOST_TOTAL_RECEIVED_PACKETS: 'int' = 3




class ENetPacketPeer__PeerState(Enum):

    STATE_DISCONNECTED: 'int' = 0
    STATE_CONNECTING: 'int' = 1
    STATE_ACKNOWLEDGING_CONNECT: 'int' = 2
    STATE_CONNECTION_PENDING: 'int' = 3
    STATE_CONNECTION_SUCCEEDED: 'int' = 4
    STATE_CONNECTED: 'int' = 5
    STATE_DISCONNECT_LATER: 'int' = 6
    STATE_DISCONNECTING: 'int' = 7
    STATE_ACKNOWLEDGING_DISCONNECT: 'int' = 8
    STATE_ZOMBIE: 'int' = 9




class ENetPacketPeer__PeerStatistic(Enum):

    PEER_PACKET_LOSS: 'int' = 0
    PEER_PACKET_LOSS_VARIANCE: 'int' = 1
    PEER_PACKET_LOSS_EPOCH: 'int' = 2
    PEER_ROUND_TRIP_TIME: 'int' = 3
    PEER_ROUND_TRIP_TIME_VARIANCE: 'int' = 4
    PEER_LAST_ROUND_TRIP_TIME: 'int' = 5
    PEER_LAST_ROUND_TRIP_TIME_VARIANCE: 'int' = 6
    PEER_PACKET_THROTTLE: 'int' = 7
    PEER_PACKET_THROTTLE_LIMIT: 'int' = 8
    PEER_PACKET_THROTTLE_COUNTER: 'int' = 9
    PEER_PACKET_THROTTLE_EPOCH: 'int' = 10
    PEER_PACKET_THROTTLE_ACCELERATION: 'int' = 11
    PEER_PACKET_THROTTLE_DECELERATION: 'int' = 12
    PEER_PACKET_THROTTLE_INTERVAL: 'int' = 13




class EditorContextMenuPlugin__ContextMenuSlot(Enum):

    CONTEXT_SLOT_SCENE_TREE: 'int' = 0
    CONTEXT_SLOT_FILESYSTEM: 'int' = 1
    CONTEXT_SLOT_SCRIPT_EDITOR: 'int' = 2
    CONTEXT_SLOT_FILESYSTEM_CREATE: 'int' = 3
    CONTEXT_SLOT_SCRIPT_EDITOR_CODE: 'int' = 4
    CONTEXT_SLOT_SCENE_TABS: 'int' = 5
    CONTEXT_SLOT_2D_EDITOR: 'int' = 6




class EditorExportPlatform__ExportMessageType(Enum):

    EXPORT_MESSAGE_NONE: 'int' = 0
    EXPORT_MESSAGE_INFO: 'int' = 1
    EXPORT_MESSAGE_WARNING: 'int' = 2
    EXPORT_MESSAGE_ERROR: 'int' = 3




class EditorExportPlatform__DebugFlags(Enum):

    DEBUG_FLAG_DUMB_CLIENT: 'int' = 1
    DEBUG_FLAG_REMOTE_DEBUG: 'int' = 2
    DEBUG_FLAG_REMOTE_DEBUG_LOCALHOST: 'int' = 4
    DEBUG_FLAG_VIEW_COLLISIONS: 'int' = 8
    DEBUG_FLAG_VIEW_NAVIGATION: 'int' = 16




class EditorExportPreset__ExportFilter(Enum):

    EXPORT_ALL_RESOURCES: 'int' = 0
    EXPORT_SELECTED_SCENES: 'int' = 1
    EXPORT_SELECTED_RESOURCES: 'int' = 2
    EXCLUDE_SELECTED_RESOURCES: 'int' = 3
    EXPORT_CUSTOMIZED: 'int' = 4




class EditorExportPreset__FileExportMode(Enum):

    MODE_FILE_NOT_CUSTOMIZED: 'int' = 0
    MODE_FILE_STRIP: 'int' = 1
    MODE_FILE_KEEP: 'int' = 2
    MODE_FILE_REMOVE: 'int' = 3




class EditorExportPreset__ScriptExportMode(Enum):

    MODE_SCRIPT_TEXT: 'int' = 0
    MODE_SCRIPT_BINARY_TOKENS: 'int' = 1
    MODE_SCRIPT_BINARY_TOKENS_COMPRESSED: 'int' = 2




class EditorFeatureProfile__Feature(Enum):

    FEATURE_3D: 'int' = 0
    FEATURE_SCRIPT: 'int' = 1
    FEATURE_ASSET_LIB: 'int' = 2
    FEATURE_SCENE_TREE: 'int' = 3
    FEATURE_NODE_DOCK: 'int' = 4
    FEATURE_FILESYSTEM_DOCK: 'int' = 5
    FEATURE_IMPORT_DOCK: 'int' = 6
    FEATURE_HISTORY_DOCK: 'int' = 7
    FEATURE_GAME: 'int' = 8
    FEATURE_MAX: 'int' = 9




class EditorFileDialog__FileMode(Enum):

    FILE_MODE_OPEN_FILE: 'int' = 0
    FILE_MODE_OPEN_FILES: 'int' = 1
    FILE_MODE_OPEN_DIR: 'int' = 2
    FILE_MODE_OPEN_ANY: 'int' = 3
    FILE_MODE_SAVE_FILE: 'int' = 4




class EditorFileDialog__Access(Enum):

    ACCESS_RESOURCES: 'int' = 0
    ACCESS_USERDATA: 'int' = 1
    ACCESS_FILESYSTEM: 'int' = 2




class EditorFileDialog__DisplayMode(Enum):

    DISPLAY_THUMBNAILS: 'int' = 0
    DISPLAY_LIST: 'int' = 1




class EditorPlugin__CustomControlContainer(Enum):

    CONTAINER_TOOLBAR: 'int' = 0
    CONTAINER_SPATIAL_EDITOR_MENU: 'int' = 1
    CONTAINER_SPATIAL_EDITOR_SIDE_LEFT: 'int' = 2
    CONTAINER_SPATIAL_EDITOR_SIDE_RIGHT: 'int' = 3
    CONTAINER_SPATIAL_EDITOR_BOTTOM: 'int' = 4
    CONTAINER_CANVAS_EDITOR_MENU: 'int' = 5
    CONTAINER_CANVAS_EDITOR_SIDE_LEFT: 'int' = 6
    CONTAINER_CANVAS_EDITOR_SIDE_RIGHT: 'int' = 7
    CONTAINER_CANVAS_EDITOR_BOTTOM: 'int' = 8
    CONTAINER_INSPECTOR_BOTTOM: 'int' = 9
    CONTAINER_PROJECT_SETTING_TAB_LEFT: 'int' = 10
    CONTAINER_PROJECT_SETTING_TAB_RIGHT: 'int' = 11




class EditorPlugin__DockSlot(Enum):

    DOCK_SLOT_LEFT_UL: 'int' = 0
    DOCK_SLOT_LEFT_BL: 'int' = 1
    DOCK_SLOT_LEFT_UR: 'int' = 2
    DOCK_SLOT_LEFT_BR: 'int' = 3
    DOCK_SLOT_RIGHT_UL: 'int' = 4
    DOCK_SLOT_RIGHT_BL: 'int' = 5
    DOCK_SLOT_RIGHT_UR: 'int' = 6
    DOCK_SLOT_RIGHT_BR: 'int' = 7
    DOCK_SLOT_MAX: 'int' = 8




class EditorPlugin__AfterGUIInput(Enum):

    AFTER_GUI_INPUT_PASS: 'int' = 0
    AFTER_GUI_INPUT_STOP: 'int' = 1
    AFTER_GUI_INPUT_CUSTOM: 'int' = 2




class EditorScenePostImportPlugin__InternalImportCategory(Enum):

    INTERNAL_IMPORT_CATEGORY_NODE: 'int' = 0
    INTERNAL_IMPORT_CATEGORY_MESH_3D_NODE: 'int' = 1
    INTERNAL_IMPORT_CATEGORY_MESH: 'int' = 2
    INTERNAL_IMPORT_CATEGORY_MATERIAL: 'int' = 3
    INTERNAL_IMPORT_CATEGORY_ANIMATION: 'int' = 4
    INTERNAL_IMPORT_CATEGORY_ANIMATION_NODE: 'int' = 5
    INTERNAL_IMPORT_CATEGORY_SKELETON_3D_NODE: 'int' = 6
    INTERNAL_IMPORT_CATEGORY_MAX: 'int' = 7




class EditorToaster__Severity(Enum):

    SEVERITY_INFO: 'int' = 0
    SEVERITY_WARNING: 'int' = 1
    SEVERITY_ERROR: 'int' = 2




class EditorUndoRedoManager__SpecialHistory(Enum):

    GLOBAL_HISTORY: 'int' = 0
    REMOTE_HISTORY: 'int' = -9
    INVALID_HISTORY: 'int' = -99




class EditorVCSInterface__ChangeType(Enum):

    CHANGE_TYPE_NEW: 'int' = 0
    CHANGE_TYPE_MODIFIED: 'int' = 1
    CHANGE_TYPE_RENAMED: 'int' = 2
    CHANGE_TYPE_DELETED: 'int' = 3
    CHANGE_TYPE_TYPECHANGE: 'int' = 4
    CHANGE_TYPE_UNMERGED: 'int' = 5




class EditorVCSInterface__TreeArea(Enum):

    TREE_AREA_COMMIT: 'int' = 0
    TREE_AREA_STAGED: 'int' = 1
    TREE_AREA_UNSTAGED: 'int' = 2




class Environment__BGMode(Enum):

    BG_CLEAR_COLOR: 'int' = 0
    BG_COLOR: 'int' = 1
    BG_SKY: 'int' = 2
    BG_CANVAS: 'int' = 3
    BG_KEEP: 'int' = 4
    BG_CAMERA_FEED: 'int' = 5
    BG_MAX: 'int' = 6




class Environment__AmbientSource(Enum):

    AMBIENT_SOURCE_BG: 'int' = 0
    AMBIENT_SOURCE_DISABLED: 'int' = 1
    AMBIENT_SOURCE_COLOR: 'int' = 2
    AMBIENT_SOURCE_SKY: 'int' = 3




class Environment__ReflectionSource(Enum):

    REFLECTION_SOURCE_BG: 'int' = 0
    REFLECTION_SOURCE_DISABLED: 'int' = 1
    REFLECTION_SOURCE_SKY: 'int' = 2




class Environment__ToneMapper(Enum):

    TONE_MAPPER_LINEAR: 'int' = 0
    TONE_MAPPER_REINHARDT: 'int' = 1
    TONE_MAPPER_FILMIC: 'int' = 2
    TONE_MAPPER_ACES: 'int' = 3
    TONE_MAPPER_AGX: 'int' = 4




class Environment__GlowBlendMode(Enum):

    GLOW_BLEND_MODE_ADDITIVE: 'int' = 0
    GLOW_BLEND_MODE_SCREEN: 'int' = 1
    GLOW_BLEND_MODE_SOFTLIGHT: 'int' = 2
    GLOW_BLEND_MODE_REPLACE: 'int' = 3
    GLOW_BLEND_MODE_MIX: 'int' = 4




class Environment__FogMode(Enum):

    FOG_MODE_EXPONENTIAL: 'int' = 0
    FOG_MODE_DEPTH: 'int' = 1




class Environment__SDFGIYScale(Enum):

    SDFGI_Y_SCALE_50_PERCENT: 'int' = 0
    SDFGI_Y_SCALE_75_PERCENT: 'int' = 1
    SDFGI_Y_SCALE_100_PERCENT: 'int' = 2




class FastNoiseLite__NoiseType(Enum):

    TYPE_VALUE: 'int' = 5
    TYPE_VALUE_CUBIC: 'int' = 4
    TYPE_PERLIN: 'int' = 3
    TYPE_CELLULAR: 'int' = 2
    TYPE_SIMPLEX: 'int' = 0
    TYPE_SIMPLEX_SMOOTH: 'int' = 1




class FastNoiseLite__FractalType(Enum):

    FRACTAL_NONE: 'int' = 0
    FRACTAL_FBM: 'int' = 1
    FRACTAL_RIDGED: 'int' = 2
    FRACTAL_PING_PONG: 'int' = 3




class FastNoiseLite__CellularDistanceFunction(Enum):

    DISTANCE_EUCLIDEAN: 'int' = 0
    DISTANCE_EUCLIDEAN_SQUARED: 'int' = 1
    DISTANCE_MANHATTAN: 'int' = 2
    DISTANCE_HYBRID: 'int' = 3




class FastNoiseLite__CellularReturnType(Enum):

    RETURN_CELL_VALUE: 'int' = 0
    RETURN_DISTANCE: 'int' = 1
    RETURN_DISTANCE2: 'int' = 2
    RETURN_DISTANCE2_ADD: 'int' = 3
    RETURN_DISTANCE2_SUB: 'int' = 4
    RETURN_DISTANCE2_MUL: 'int' = 5
    RETURN_DISTANCE2_DIV: 'int' = 6




class FastNoiseLite__DomainWarpType(Enum):

    DOMAIN_WARP_SIMPLEX: 'int' = 0
    DOMAIN_WARP_SIMPLEX_REDUCED: 'int' = 1
    DOMAIN_WARP_BASIC_GRID: 'int' = 2




class FastNoiseLite__DomainWarpFractalType(Enum):

    DOMAIN_WARP_FRACTAL_NONE: 'int' = 0
    DOMAIN_WARP_FRACTAL_PROGRESSIVE: 'int' = 1
    DOMAIN_WARP_FRACTAL_INDEPENDENT: 'int' = 2




class FileAccess__ModeFlags(Enum):

    READ: 'int' = 1
    WRITE: 'int' = 2
    READ_WRITE: 'int' = 3
    WRITE_READ: 'int' = 7




class FileAccess__CompressionMode(Enum):

    COMPRESSION_FASTLZ: 'int' = 0
    COMPRESSION_DEFLATE: 'int' = 1
    COMPRESSION_ZSTD: 'int' = 2
    COMPRESSION_GZIP: 'int' = 3
    COMPRESSION_BROTLI: 'int' = 4




class FileAccess__UnixPermissionFlags(Enum):

    UNIX_READ_OWNER: 'int' = 256
    UNIX_WRITE_OWNER: 'int' = 128
    UNIX_EXECUTE_OWNER: 'int' = 64
    UNIX_READ_GROUP: 'int' = 32
    UNIX_WRITE_GROUP: 'int' = 16
    UNIX_EXECUTE_GROUP: 'int' = 8
    UNIX_READ_OTHER: 'int' = 4
    UNIX_WRITE_OTHER: 'int' = 2
    UNIX_EXECUTE_OTHER: 'int' = 1
    UNIX_SET_USER_ID: 'int' = 2048
    UNIX_SET_GROUP_ID: 'int' = 1024
    UNIX_RESTRICTED_DELETE: 'int' = 512




class FileDialog__FileMode(Enum):

    FILE_MODE_OPEN_FILE: 'int' = 0
    FILE_MODE_OPEN_FILES: 'int' = 1
    FILE_MODE_OPEN_DIR: 'int' = 2
    FILE_MODE_OPEN_ANY: 'int' = 3
    FILE_MODE_SAVE_FILE: 'int' = 4




class FileDialog__Access(Enum):

    ACCESS_RESOURCES: 'int' = 0
    ACCESS_USERDATA: 'int' = 1
    ACCESS_FILESYSTEM: 'int' = 2




class FlowContainer__AlignmentMode(Enum):

    ALIGNMENT_BEGIN: 'int' = 0
    ALIGNMENT_CENTER: 'int' = 1
    ALIGNMENT_END: 'int' = 2




class FlowContainer__LastWrapAlignmentMode(Enum):

    LAST_WRAP_ALIGNMENT_INHERIT: 'int' = 0
    LAST_WRAP_ALIGNMENT_BEGIN: 'int' = 1
    LAST_WRAP_ALIGNMENT_CENTER: 'int' = 2
    LAST_WRAP_ALIGNMENT_END: 'int' = 3




class GDExtension__InitializationLevel(Enum):

    INITIALIZATION_LEVEL_CORE: 'int' = 0
    INITIALIZATION_LEVEL_SERVERS: 'int' = 1
    INITIALIZATION_LEVEL_SCENE: 'int' = 2
    INITIALIZATION_LEVEL_EDITOR: 'int' = 3




class GDExtensionManager__LoadStatus(Enum):

    LOAD_STATUS_OK: 'int' = 0
    LOAD_STATUS_FAILED: 'int' = 1
    LOAD_STATUS_ALREADY_LOADED: 'int' = 2
    LOAD_STATUS_NOT_LOADED: 'int' = 3
    LOAD_STATUS_NEEDS_RESTART: 'int' = 4




class GLTFAccessor__GLTFAccessorType(Enum):

    TYPE_SCALAR: 'int' = 0
    TYPE_VEC2: 'int' = 1
    TYPE_VEC3: 'int' = 2
    TYPE_VEC4: 'int' = 3
    TYPE_MAT2: 'int' = 4
    TYPE_MAT3: 'int' = 5
    TYPE_MAT4: 'int' = 6




class GLTFAccessor__GLTFComponentType(Enum):

    COMPONENT_TYPE_NONE: 'int' = 0
    COMPONENT_TYPE_SIGNED_BYTE: 'int' = 5120
    COMPONENT_TYPE_UNSIGNED_BYTE: 'int' = 5121
    COMPONENT_TYPE_SIGNED_SHORT: 'int' = 5122
    COMPONENT_TYPE_UNSIGNED_SHORT: 'int' = 5123
    COMPONENT_TYPE_SIGNED_INT: 'int' = 5124
    COMPONENT_TYPE_UNSIGNED_INT: 'int' = 5125
    COMPONENT_TYPE_SINGLE_FLOAT: 'int' = 5126
    COMPONENT_TYPE_DOUBLE_FLOAT: 'int' = 5130
    COMPONENT_TYPE_HALF_FLOAT: 'int' = 5131
    COMPONENT_TYPE_SIGNED_LONG: 'int' = 5134
    COMPONENT_TYPE_UNSIGNED_LONG: 'int' = 5135




class GLTFDocument__RootNodeMode(Enum):

    ROOT_NODE_MODE_SINGLE_ROOT: 'int' = 0
    ROOT_NODE_MODE_KEEP_ROOT: 'int' = 1
    ROOT_NODE_MODE_MULTI_ROOT: 'int' = 2




class GLTFObjectModelProperty__GLTFObjectModelType(Enum):

    GLTF_OBJECT_MODEL_TYPE_UNKNOWN: 'int' = 0
    GLTF_OBJECT_MODEL_TYPE_BOOL: 'int' = 1
    GLTF_OBJECT_MODEL_TYPE_FLOAT: 'int' = 2
    GLTF_OBJECT_MODEL_TYPE_FLOAT_ARRAY: 'int' = 3
    GLTF_OBJECT_MODEL_TYPE_FLOAT2: 'int' = 4
    GLTF_OBJECT_MODEL_TYPE_FLOAT3: 'int' = 5
    GLTF_OBJECT_MODEL_TYPE_FLOAT4: 'int' = 6
    GLTF_OBJECT_MODEL_TYPE_FLOAT2X2: 'int' = 7
    GLTF_OBJECT_MODEL_TYPE_FLOAT3X3: 'int' = 8
    GLTF_OBJECT_MODEL_TYPE_FLOAT4X4: 'int' = 9
    GLTF_OBJECT_MODEL_TYPE_INT: 'int' = 10




class GPUParticles2D__DrawOrder(Enum):

    DRAW_ORDER_INDEX: 'int' = 0
    DRAW_ORDER_LIFETIME: 'int' = 1
    DRAW_ORDER_REVERSE_LIFETIME: 'int' = 2




class GPUParticles2D__EmitFlags(Enum):

    EMIT_FLAG_POSITION: 'int' = 1
    EMIT_FLAG_ROTATION_SCALE: 'int' = 2
    EMIT_FLAG_VELOCITY: 'int' = 4
    EMIT_FLAG_COLOR: 'int' = 8
    EMIT_FLAG_CUSTOM: 'int' = 16




class GPUParticles3D__DrawOrder(Enum):

    DRAW_ORDER_INDEX: 'int' = 0
    DRAW_ORDER_LIFETIME: 'int' = 1
    DRAW_ORDER_REVERSE_LIFETIME: 'int' = 2
    DRAW_ORDER_VIEW_DEPTH: 'int' = 3




class GPUParticles3D__EmitFlags(Enum):

    EMIT_FLAG_POSITION: 'int' = 1
    EMIT_FLAG_ROTATION_SCALE: 'int' = 2
    EMIT_FLAG_VELOCITY: 'int' = 4
    EMIT_FLAG_COLOR: 'int' = 8
    EMIT_FLAG_CUSTOM: 'int' = 16




class GPUParticles3D__TransformAlign(Enum):

    TRANSFORM_ALIGN_DISABLED: 'int' = 0
    TRANSFORM_ALIGN_Z_BILLBOARD: 'int' = 1
    TRANSFORM_ALIGN_Y_TO_VELOCITY: 'int' = 2
    TRANSFORM_ALIGN_Z_BILLBOARD_Y_TO_VELOCITY: 'int' = 3




class GPUParticlesCollisionHeightField3D__Resolution(Enum):

    RESOLUTION_256: 'int' = 0
    RESOLUTION_512: 'int' = 1
    RESOLUTION_1024: 'int' = 2
    RESOLUTION_2048: 'int' = 3
    RESOLUTION_4096: 'int' = 4
    RESOLUTION_8192: 'int' = 5
    RESOLUTION_MAX: 'int' = 6




class GPUParticlesCollisionHeightField3D__UpdateMode(Enum):

    UPDATE_MODE_WHEN_MOVED: 'int' = 0
    UPDATE_MODE_ALWAYS: 'int' = 1




class GPUParticlesCollisionSDF3D__Resolution(Enum):

    RESOLUTION_16: 'int' = 0
    RESOLUTION_32: 'int' = 1
    RESOLUTION_64: 'int' = 2
    RESOLUTION_128: 'int' = 3
    RESOLUTION_256: 'int' = 4
    RESOLUTION_512: 'int' = 5
    RESOLUTION_MAX: 'int' = 6




class Generic6DOFJoint3D__Param(Enum):

    PARAM_LINEAR_LOWER_LIMIT: 'int' = 0
    PARAM_LINEAR_UPPER_LIMIT: 'int' = 1
    PARAM_LINEAR_LIMIT_SOFTNESS: 'int' = 2
    PARAM_LINEAR_RESTITUTION: 'int' = 3
    PARAM_LINEAR_DAMPING: 'int' = 4
    PARAM_LINEAR_MOTOR_TARGET_VELOCITY: 'int' = 5
    PARAM_LINEAR_MOTOR_FORCE_LIMIT: 'int' = 6
    PARAM_LINEAR_SPRING_STIFFNESS: 'int' = 7
    PARAM_LINEAR_SPRING_DAMPING: 'int' = 8
    PARAM_LINEAR_SPRING_EQUILIBRIUM_POINT: 'int' = 9
    PARAM_ANGULAR_LOWER_LIMIT: 'int' = 10
    PARAM_ANGULAR_UPPER_LIMIT: 'int' = 11
    PARAM_ANGULAR_LIMIT_SOFTNESS: 'int' = 12
    PARAM_ANGULAR_DAMPING: 'int' = 13
    PARAM_ANGULAR_RESTITUTION: 'int' = 14
    PARAM_ANGULAR_FORCE_LIMIT: 'int' = 15
    PARAM_ANGULAR_ERP: 'int' = 16
    PARAM_ANGULAR_MOTOR_TARGET_VELOCITY: 'int' = 17
    PARAM_ANGULAR_MOTOR_FORCE_LIMIT: 'int' = 18
    PARAM_ANGULAR_SPRING_STIFFNESS: 'int' = 19
    PARAM_ANGULAR_SPRING_DAMPING: 'int' = 20
    PARAM_ANGULAR_SPRING_EQUILIBRIUM_POINT: 'int' = 21
    PARAM_MAX: 'int' = 22




class Generic6DOFJoint3D__Flag(Enum):

    FLAG_ENABLE_LINEAR_LIMIT: 'int' = 0
    FLAG_ENABLE_ANGULAR_LIMIT: 'int' = 1
    FLAG_ENABLE_LINEAR_SPRING: 'int' = 3
    FLAG_ENABLE_ANGULAR_SPRING: 'int' = 2
    FLAG_ENABLE_MOTOR: 'int' = 4
    FLAG_ENABLE_LINEAR_MOTOR: 'int' = 5
    FLAG_MAX: 'int' = 6




class Geometry2D__PolyBooleanOperation(Enum):

    OPERATION_UNION: 'int' = 0
    OPERATION_DIFFERENCE: 'int' = 1
    OPERATION_INTERSECTION: 'int' = 2
    OPERATION_XOR: 'int' = 3




class Geometry2D__PolyJoinType(Enum):

    JOIN_SQUARE: 'int' = 0
    JOIN_ROUND: 'int' = 1
    JOIN_MITER: 'int' = 2




class Geometry2D__PolyEndType(Enum):

    END_POLYGON: 'int' = 0
    END_JOINED: 'int' = 1
    END_BUTT: 'int' = 2
    END_SQUARE: 'int' = 3
    END_ROUND: 'int' = 4




class GeometryInstance3D__ShadowCastingSetting(Enum):

    SHADOW_CASTING_SETTING_OFF: 'int' = 0
    SHADOW_CASTING_SETTING_ON: 'int' = 1
    SHADOW_CASTING_SETTING_DOUBLE_SIDED: 'int' = 2
    SHADOW_CASTING_SETTING_SHADOWS_ONLY: 'int' = 3




class GeometryInstance3D__GIMode(Enum):

    GI_MODE_DISABLED: 'int' = 0
    GI_MODE_STATIC: 'int' = 1
    GI_MODE_DYNAMIC: 'int' = 2




class GeometryInstance3D__LightmapScale(Enum):

    LIGHTMAP_SCALE_1X: 'int' = 0
    LIGHTMAP_SCALE_2X: 'int' = 1
    LIGHTMAP_SCALE_4X: 'int' = 2
    LIGHTMAP_SCALE_8X: 'int' = 3
    LIGHTMAP_SCALE_MAX: 'int' = 4




class GeometryInstance3D__VisibilityRangeFadeMode(Enum):

    VISIBILITY_RANGE_FADE_DISABLED: 'int' = 0
    VISIBILITY_RANGE_FADE_SELF: 'int' = 1
    VISIBILITY_RANGE_FADE_DEPENDENCIES: 'int' = 2




class Gradient__InterpolationMode(Enum):

    GRADIENT_INTERPOLATE_LINEAR: 'int' = 0
    GRADIENT_INTERPOLATE_CONSTANT: 'int' = 1
    GRADIENT_INTERPOLATE_CUBIC: 'int' = 2




class Gradient__ColorSpace(Enum):

    GRADIENT_COLOR_SPACE_SRGB: 'int' = 0
    GRADIENT_COLOR_SPACE_LINEAR_SRGB: 'int' = 1
    GRADIENT_COLOR_SPACE_OKLAB: 'int' = 2




class GradientTexture2D__Fill(Enum):

    FILL_LINEAR: 'int' = 0
    FILL_RADIAL: 'int' = 1
    FILL_SQUARE: 'int' = 2




class GradientTexture2D__Repeat(Enum):

    REPEAT_NONE: 'int' = 0
    REPEAT: 'int' = 1
    REPEAT_MIRROR: 'int' = 2




class GraphEdit__PanningScheme(Enum):

    SCROLL_ZOOMS: 'int' = 0
    SCROLL_PANS: 'int' = 1




class GraphEdit__GridPattern(Enum):

    GRID_PATTERN_LINES: 'int' = 0
    GRID_PATTERN_DOTS: 'int' = 1




class HTTPClient__Method(Enum):

    METHOD_GET: 'int' = 0
    METHOD_HEAD: 'int' = 1
    METHOD_POST: 'int' = 2
    METHOD_PUT: 'int' = 3
    METHOD_DELETE: 'int' = 4
    METHOD_OPTIONS: 'int' = 5
    METHOD_TRACE: 'int' = 6
    METHOD_CONNECT: 'int' = 7
    METHOD_PATCH: 'int' = 8
    METHOD_MAX: 'int' = 9




class HTTPClient__Status(Enum):

    STATUS_DISCONNECTED: 'int' = 0
    STATUS_RESOLVING: 'int' = 1
    STATUS_CANT_RESOLVE: 'int' = 2
    STATUS_CONNECTING: 'int' = 3
    STATUS_CANT_CONNECT: 'int' = 4
    STATUS_CONNECTED: 'int' = 5
    STATUS_REQUESTING: 'int' = 6
    STATUS_BODY: 'int' = 7
    STATUS_CONNECTION_ERROR: 'int' = 8
    STATUS_TLS_HANDSHAKE_ERROR: 'int' = 9




class HTTPClient__ResponseCode(Enum):

    RESPONSE_CONTINUE: 'int' = 100
    RESPONSE_SWITCHING_PROTOCOLS: 'int' = 101
    RESPONSE_PROCESSING: 'int' = 102
    RESPONSE_OK: 'int' = 200
    RESPONSE_CREATED: 'int' = 201
    RESPONSE_ACCEPTED: 'int' = 202
    RESPONSE_NON_AUTHORITATIVE_INFORMATION: 'int' = 203
    RESPONSE_NO_CONTENT: 'int' = 204
    RESPONSE_RESET_CONTENT: 'int' = 205
    RESPONSE_PARTIAL_CONTENT: 'int' = 206
    RESPONSE_MULTI_STATUS: 'int' = 207
    RESPONSE_ALREADY_REPORTED: 'int' = 208
    RESPONSE_IM_USED: 'int' = 226
    RESPONSE_MULTIPLE_CHOICES: 'int' = 300
    RESPONSE_MOVED_PERMANENTLY: 'int' = 301
    RESPONSE_FOUND: 'int' = 302
    RESPONSE_SEE_OTHER: 'int' = 303
    RESPONSE_NOT_MODIFIED: 'int' = 304
    RESPONSE_USE_PROXY: 'int' = 305
    RESPONSE_SWITCH_PROXY: 'int' = 306
    RESPONSE_TEMPORARY_REDIRECT: 'int' = 307
    RESPONSE_PERMANENT_REDIRECT: 'int' = 308
    RESPONSE_BAD_REQUEST: 'int' = 400
    RESPONSE_UNAUTHORIZED: 'int' = 401
    RESPONSE_PAYMENT_REQUIRED: 'int' = 402
    RESPONSE_FORBIDDEN: 'int' = 403
    RESPONSE_NOT_FOUND: 'int' = 404
    RESPONSE_METHOD_NOT_ALLOWED: 'int' = 405
    RESPONSE_NOT_ACCEPTABLE: 'int' = 406
    RESPONSE_PROXY_AUTHENTICATION_REQUIRED: 'int' = 407
    RESPONSE_REQUEST_TIMEOUT: 'int' = 408
    RESPONSE_CONFLICT: 'int' = 409
    RESPONSE_GONE: 'int' = 410
    RESPONSE_LENGTH_REQUIRED: 'int' = 411
    RESPONSE_PRECONDITION_FAILED: 'int' = 412
    RESPONSE_REQUEST_ENTITY_TOO_LARGE: 'int' = 413
    RESPONSE_REQUEST_URI_TOO_LONG: 'int' = 414
    RESPONSE_UNSUPPORTED_MEDIA_TYPE: 'int' = 415
    RESPONSE_REQUESTED_RANGE_NOT_SATISFIABLE: 'int' = 416
    RESPONSE_EXPECTATION_FAILED: 'int' = 417
    RESPONSE_IM_A_TEAPOT: 'int' = 418
    RESPONSE_MISDIRECTED_REQUEST: 'int' = 421
    RESPONSE_UNPROCESSABLE_ENTITY: 'int' = 422
    RESPONSE_LOCKED: 'int' = 423
    RESPONSE_FAILED_DEPENDENCY: 'int' = 424
    RESPONSE_UPGRADE_REQUIRED: 'int' = 426
    RESPONSE_PRECONDITION_REQUIRED: 'int' = 428
    RESPONSE_TOO_MANY_REQUESTS: 'int' = 429
    RESPONSE_REQUEST_HEADER_FIELDS_TOO_LARGE: 'int' = 431
    RESPONSE_UNAVAILABLE_FOR_LEGAL_REASONS: 'int' = 451
    RESPONSE_INTERNAL_SERVER_ERROR: 'int' = 500
    RESPONSE_NOT_IMPLEMENTED: 'int' = 501
    RESPONSE_BAD_GATEWAY: 'int' = 502
    RESPONSE_SERVICE_UNAVAILABLE: 'int' = 503
    RESPONSE_GATEWAY_TIMEOUT: 'int' = 504
    RESPONSE_HTTP_VERSION_NOT_SUPPORTED: 'int' = 505
    RESPONSE_VARIANT_ALSO_NEGOTIATES: 'int' = 506
    RESPONSE_INSUFFICIENT_STORAGE: 'int' = 507
    RESPONSE_LOOP_DETECTED: 'int' = 508
    RESPONSE_NOT_EXTENDED: 'int' = 510
    RESPONSE_NETWORK_AUTH_REQUIRED: 'int' = 511




class HTTPRequest__Result(Enum):

    RESULT_SUCCESS: 'int' = 0
    RESULT_CHUNKED_BODY_SIZE_MISMATCH: 'int' = 1
    RESULT_CANT_CONNECT: 'int' = 2
    RESULT_CANT_RESOLVE: 'int' = 3
    RESULT_CONNECTION_ERROR: 'int' = 4
    RESULT_TLS_HANDSHAKE_ERROR: 'int' = 5
    RESULT_NO_RESPONSE: 'int' = 6
    RESULT_BODY_SIZE_LIMIT_EXCEEDED: 'int' = 7
    RESULT_BODY_DECOMPRESS_FAILED: 'int' = 8
    RESULT_REQUEST_FAILED: 'int' = 9
    RESULT_DOWNLOAD_FILE_CANT_OPEN: 'int' = 10
    RESULT_DOWNLOAD_FILE_WRITE_ERROR: 'int' = 11
    RESULT_REDIRECT_LIMIT_REACHED: 'int' = 12
    RESULT_TIMEOUT: 'int' = 13




class HashingContext__HashType(Enum):

    HASH_MD5: 'int' = 0
    HASH_SHA1: 'int' = 1
    HASH_SHA256: 'int' = 2




class HingeJoint3D__Param(Enum):

    PARAM_BIAS: 'int' = 0
    PARAM_LIMIT_UPPER: 'int' = 1
    PARAM_LIMIT_LOWER: 'int' = 2
    PARAM_LIMIT_BIAS: 'int' = 3
    PARAM_LIMIT_SOFTNESS: 'int' = 4
    PARAM_LIMIT_RELAXATION: 'int' = 5
    PARAM_MOTOR_TARGET_VELOCITY: 'int' = 6
    PARAM_MOTOR_MAX_IMPULSE: 'int' = 7
    PARAM_MAX: 'int' = 8




class HingeJoint3D__Flag(Enum):

    FLAG_USE_LIMIT: 'int' = 0
    FLAG_ENABLE_MOTOR: 'int' = 1
    FLAG_MAX: 'int' = 2




class IP__ResolverStatus(Enum):

    RESOLVER_STATUS_NONE: 'int' = 0
    RESOLVER_STATUS_WAITING: 'int' = 1
    RESOLVER_STATUS_DONE: 'int' = 2
    RESOLVER_STATUS_ERROR: 'int' = 3




class IP__Type(Enum):

    TYPE_NONE: 'int' = 0
    TYPE_IPV4: 'int' = 1
    TYPE_IPV6: 'int' = 2
    TYPE_ANY: 'int' = 3




class Image__Format(Enum):

    FORMAT_L8: 'int' = 0
    FORMAT_LA8: 'int' = 1
    FORMAT_R8: 'int' = 2
    FORMAT_RG8: 'int' = 3
    FORMAT_RGB8: 'int' = 4
    FORMAT_RGBA8: 'int' = 5
    FORMAT_RGBA4444: 'int' = 6
    FORMAT_RGB565: 'int' = 7
    FORMAT_RF: 'int' = 8
    FORMAT_RGF: 'int' = 9
    FORMAT_RGBF: 'int' = 10
    FORMAT_RGBAF: 'int' = 11
    FORMAT_RH: 'int' = 12
    FORMAT_RGH: 'int' = 13
    FORMAT_RGBH: 'int' = 14
    FORMAT_RGBAH: 'int' = 15
    FORMAT_RGBE9995: 'int' = 16
    FORMAT_DXT1: 'int' = 17
    FORMAT_DXT3: 'int' = 18
    FORMAT_DXT5: 'int' = 19
    FORMAT_RGTC_R: 'int' = 20
    FORMAT_RGTC_RG: 'int' = 21
    FORMAT_BPTC_RGBA: 'int' = 22
    FORMAT_BPTC_RGBF: 'int' = 23
    FORMAT_BPTC_RGBFU: 'int' = 24
    FORMAT_ETC: 'int' = 25
    FORMAT_ETC2_R11: 'int' = 26
    FORMAT_ETC2_R11S: 'int' = 27
    FORMAT_ETC2_RG11: 'int' = 28
    FORMAT_ETC2_RG11S: 'int' = 29
    FORMAT_ETC2_RGB8: 'int' = 30
    FORMAT_ETC2_RGBA8: 'int' = 31
    FORMAT_ETC2_RGB8A1: 'int' = 32
    FORMAT_ETC2_RA_AS_RG: 'int' = 33
    FORMAT_DXT5_RA_AS_RG: 'int' = 34
    FORMAT_ASTC_4x4: 'int' = 35
    FORMAT_ASTC_4x4_HDR: 'int' = 36
    FORMAT_ASTC_8x8: 'int' = 37
    FORMAT_ASTC_8x8_HDR: 'int' = 38
    FORMAT_MAX: 'int' = 39




class Image__Interpolation(Enum):

    INTERPOLATE_NEAREST: 'int' = 0
    INTERPOLATE_BILINEAR: 'int' = 1
    INTERPOLATE_CUBIC: 'int' = 2
    INTERPOLATE_TRILINEAR: 'int' = 3
    INTERPOLATE_LANCZOS: 'int' = 4




class Image__AlphaMode(Enum):

    ALPHA_NONE: 'int' = 0
    ALPHA_BIT: 'int' = 1
    ALPHA_BLEND: 'int' = 2




class Image__CompressMode(Enum):

    COMPRESS_S3TC: 'int' = 0
    COMPRESS_ETC: 'int' = 1
    COMPRESS_ETC2: 'int' = 2
    COMPRESS_BPTC: 'int' = 3
    COMPRESS_ASTC: 'int' = 4
    COMPRESS_MAX: 'int' = 5




class Image__UsedChannels(Enum):

    USED_CHANNELS_L: 'int' = 0
    USED_CHANNELS_LA: 'int' = 1
    USED_CHANNELS_R: 'int' = 2
    USED_CHANNELS_RG: 'int' = 3
    USED_CHANNELS_RGB: 'int' = 4
    USED_CHANNELS_RGBA: 'int' = 5




class Image__CompressSource(Enum):

    COMPRESS_SOURCE_GENERIC: 'int' = 0
    COMPRESS_SOURCE_SRGB: 'int' = 1
    COMPRESS_SOURCE_NORMAL: 'int' = 2




class Image__ASTCFormat(Enum):

    ASTC_FORMAT_4x4: 'int' = 0
    ASTC_FORMAT_8x8: 'int' = 1




class ImageFormatLoader__LoaderFlags(Enum):

    FLAG_NONE: 'int' = 0
    FLAG_FORCE_LINEAR: 'int' = 1
    FLAG_CONVERT_COLORS: 'int' = 2




class Input__MouseMode(Enum):

    MOUSE_MODE_VISIBLE: 'int' = 0
    MOUSE_MODE_HIDDEN: 'int' = 1
    MOUSE_MODE_CAPTURED: 'int' = 2
    MOUSE_MODE_CONFINED: 'int' = 3
    MOUSE_MODE_CONFINED_HIDDEN: 'int' = 4
    MOUSE_MODE_MAX: 'int' = 5




class Input__CursorShape(Enum):

    CURSOR_ARROW: 'int' = 0
    CURSOR_IBEAM: 'int' = 1
    CURSOR_POINTING_HAND: 'int' = 2
    CURSOR_CROSS: 'int' = 3
    CURSOR_WAIT: 'int' = 4
    CURSOR_BUSY: 'int' = 5
    CURSOR_DRAG: 'int' = 6
    CURSOR_CAN_DROP: 'int' = 7
    CURSOR_FORBIDDEN: 'int' = 8
    CURSOR_VSIZE: 'int' = 9
    CURSOR_HSIZE: 'int' = 10
    CURSOR_BDIAGSIZE: 'int' = 11
    CURSOR_FDIAGSIZE: 'int' = 12
    CURSOR_MOVE: 'int' = 13
    CURSOR_VSPLIT: 'int' = 14
    CURSOR_HSPLIT: 'int' = 15
    CURSOR_HELP: 'int' = 16




class ItemList__IconMode(Enum):

    ICON_MODE_TOP: 'int' = 0
    ICON_MODE_LEFT: 'int' = 1




class ItemList__SelectMode(Enum):

    SELECT_SINGLE: 'int' = 0
    SELECT_MULTI: 'int' = 1
    SELECT_TOGGLE: 'int' = 2




class JSONRPC__ErrorCode(Enum):

    PARSE_ERROR: 'int' = -32700
    INVALID_REQUEST: 'int' = -32600
    METHOD_NOT_FOUND: 'int' = -32601
    INVALID_PARAMS: 'int' = -32602
    INTERNAL_ERROR: 'int' = -32603




class Label3D__DrawFlags(Enum):

    FLAG_SHADED: 'int' = 0
    FLAG_DOUBLE_SIDED: 'int' = 1
    FLAG_DISABLE_DEPTH_TEST: 'int' = 2
    FLAG_FIXED_SIZE: 'int' = 3
    FLAG_MAX: 'int' = 4




class Label3D__AlphaCutMode(Enum):

    ALPHA_CUT_DISABLED: 'int' = 0
    ALPHA_CUT_DISCARD: 'int' = 1
    ALPHA_CUT_OPAQUE_PREPASS: 'int' = 2
    ALPHA_CUT_HASH: 'int' = 3




class Light2D__ShadowFilter(Enum):

    SHADOW_FILTER_NONE: 'int' = 0
    SHADOW_FILTER_PCF5: 'int' = 1
    SHADOW_FILTER_PCF13: 'int' = 2




class Light2D__BlendMode(Enum):

    BLEND_MODE_ADD: 'int' = 0
    BLEND_MODE_SUB: 'int' = 1
    BLEND_MODE_MIX: 'int' = 2




class Light3D__Param(Enum):

    PARAM_ENERGY: 'int' = 0
    PARAM_INDIRECT_ENERGY: 'int' = 1
    PARAM_VOLUMETRIC_FOG_ENERGY: 'int' = 2
    PARAM_SPECULAR: 'int' = 3
    PARAM_RANGE: 'int' = 4
    PARAM_SIZE: 'int' = 5
    PARAM_ATTENUATION: 'int' = 6
    PARAM_SPOT_ANGLE: 'int' = 7
    PARAM_SPOT_ATTENUATION: 'int' = 8
    PARAM_SHADOW_MAX_DISTANCE: 'int' = 9
    PARAM_SHADOW_SPLIT_1_OFFSET: 'int' = 10
    PARAM_SHADOW_SPLIT_2_OFFSET: 'int' = 11
    PARAM_SHADOW_SPLIT_3_OFFSET: 'int' = 12
    PARAM_SHADOW_FADE_START: 'int' = 13
    PARAM_SHADOW_NORMAL_BIAS: 'int' = 14
    PARAM_SHADOW_BIAS: 'int' = 15
    PARAM_SHADOW_PANCAKE_SIZE: 'int' = 16
    PARAM_SHADOW_OPACITY: 'int' = 17
    PARAM_SHADOW_BLUR: 'int' = 18
    PARAM_TRANSMITTANCE_BIAS: 'int' = 19
    PARAM_INTENSITY: 'int' = 20
    PARAM_MAX: 'int' = 21




class Light3D__BakeMode(Enum):

    BAKE_DISABLED: 'int' = 0
    BAKE_STATIC: 'int' = 1
    BAKE_DYNAMIC: 'int' = 2




class LightmapGI__BakeQuality(Enum):

    BAKE_QUALITY_LOW: 'int' = 0
    BAKE_QUALITY_MEDIUM: 'int' = 1
    BAKE_QUALITY_HIGH: 'int' = 2
    BAKE_QUALITY_ULTRA: 'int' = 3




class LightmapGI__GenerateProbes(Enum):

    GENERATE_PROBES_DISABLED: 'int' = 0
    GENERATE_PROBES_SUBDIV_4: 'int' = 1
    GENERATE_PROBES_SUBDIV_8: 'int' = 2
    GENERATE_PROBES_SUBDIV_16: 'int' = 3
    GENERATE_PROBES_SUBDIV_32: 'int' = 4




class LightmapGI__BakeError(Enum):

    BAKE_ERROR_OK: 'int' = 0
    BAKE_ERROR_NO_SCENE_ROOT: 'int' = 1
    BAKE_ERROR_FOREIGN_DATA: 'int' = 2
    BAKE_ERROR_NO_LIGHTMAPPER: 'int' = 3
    BAKE_ERROR_NO_SAVE_PATH: 'int' = 4
    BAKE_ERROR_NO_MESHES: 'int' = 5
    BAKE_ERROR_MESHES_INVALID: 'int' = 6
    BAKE_ERROR_CANT_CREATE_IMAGE: 'int' = 7
    BAKE_ERROR_USER_ABORTED: 'int' = 8
    BAKE_ERROR_TEXTURE_SIZE_TOO_SMALL: 'int' = 9
    BAKE_ERROR_LIGHTMAP_TOO_SMALL: 'int' = 10
    BAKE_ERROR_ATLAS_TOO_SMALL: 'int' = 11




class LightmapGI__EnvironmentMode(Enum):

    ENVIRONMENT_MODE_DISABLED: 'int' = 0
    ENVIRONMENT_MODE_SCENE: 'int' = 1
    ENVIRONMENT_MODE_CUSTOM_SKY: 'int' = 2
    ENVIRONMENT_MODE_CUSTOM_COLOR: 'int' = 3




class LightmapGIData__ShadowmaskMode(Enum):

    SHADOWMASK_MODE_NONE: 'int' = 0
    SHADOWMASK_MODE_REPLACE: 'int' = 1
    SHADOWMASK_MODE_OVERLAY: 'int' = 2




class Line2D__LineJointMode(Enum):

    LINE_JOINT_SHARP: 'int' = 0
    LINE_JOINT_BEVEL: 'int' = 1
    LINE_JOINT_ROUND: 'int' = 2




class Line2D__LineCapMode(Enum):

    LINE_CAP_NONE: 'int' = 0
    LINE_CAP_BOX: 'int' = 1
    LINE_CAP_ROUND: 'int' = 2




class Line2D__LineTextureMode(Enum):

    LINE_TEXTURE_NONE: 'int' = 0
    LINE_TEXTURE_TILE: 'int' = 1
    LINE_TEXTURE_STRETCH: 'int' = 2




class LineEdit__MenuItems(Enum):

    MENU_CUT: 'int' = 0
    MENU_COPY: 'int' = 1
    MENU_PASTE: 'int' = 2
    MENU_CLEAR: 'int' = 3
    MENU_SELECT_ALL: 'int' = 4
    MENU_UNDO: 'int' = 5
    MENU_REDO: 'int' = 6
    MENU_SUBMENU_TEXT_DIR: 'int' = 7
    MENU_DIR_INHERITED: 'int' = 8
    MENU_DIR_AUTO: 'int' = 9
    MENU_DIR_LTR: 'int' = 10
    MENU_DIR_RTL: 'int' = 11
    MENU_DISPLAY_UCC: 'int' = 12
    MENU_SUBMENU_INSERT_UCC: 'int' = 13
    MENU_INSERT_LRM: 'int' = 14
    MENU_INSERT_RLM: 'int' = 15
    MENU_INSERT_LRE: 'int' = 16
    MENU_INSERT_RLE: 'int' = 17
    MENU_INSERT_LRO: 'int' = 18
    MENU_INSERT_RLO: 'int' = 19
    MENU_INSERT_PDF: 'int' = 20
    MENU_INSERT_ALM: 'int' = 21
    MENU_INSERT_LRI: 'int' = 22
    MENU_INSERT_RLI: 'int' = 23
    MENU_INSERT_FSI: 'int' = 24
    MENU_INSERT_PDI: 'int' = 25
    MENU_INSERT_ZWJ: 'int' = 26
    MENU_INSERT_ZWNJ: 'int' = 27
    MENU_INSERT_WJ: 'int' = 28
    MENU_INSERT_SHY: 'int' = 29
    MENU_EMOJI_AND_SYMBOL: 'int' = 30
    MENU_MAX: 'int' = 31




class LineEdit__VirtualKeyboardType(Enum):

    KEYBOARD_TYPE_DEFAULT: 'int' = 0
    KEYBOARD_TYPE_MULTILINE: 'int' = 1
    KEYBOARD_TYPE_NUMBER: 'int' = 2
    KEYBOARD_TYPE_NUMBER_DECIMAL: 'int' = 3
    KEYBOARD_TYPE_PHONE: 'int' = 4
    KEYBOARD_TYPE_EMAIL_ADDRESS: 'int' = 5
    KEYBOARD_TYPE_PASSWORD: 'int' = 6
    KEYBOARD_TYPE_URL: 'int' = 7




class LinkButton__UnderlineMode(Enum):

    UNDERLINE_MODE_ALWAYS: 'int' = 0
    UNDERLINE_MODE_ON_HOVER: 'int' = 1
    UNDERLINE_MODE_NEVER: 'int' = 2




class LookAtModifier3D__OriginFrom(Enum):

    ORIGIN_FROM_SELF: 'int' = 0
    ORIGIN_FROM_SPECIFIC_BONE: 'int' = 1
    ORIGIN_FROM_EXTERNAL_NODE: 'int' = 2




class Mesh__PrimitiveType(Enum):

    PRIMITIVE_POINTS: 'int' = 0
    PRIMITIVE_LINES: 'int' = 1
    PRIMITIVE_LINE_STRIP: 'int' = 2
    PRIMITIVE_TRIANGLES: 'int' = 3
    PRIMITIVE_TRIANGLE_STRIP: 'int' = 4




class Mesh__ArrayType(Enum):

    ARRAY_VERTEX: 'int' = 0
    ARRAY_NORMAL: 'int' = 1
    ARRAY_TANGENT: 'int' = 2
    ARRAY_COLOR: 'int' = 3
    ARRAY_TEX_UV: 'int' = 4
    ARRAY_TEX_UV2: 'int' = 5
    ARRAY_CUSTOM0: 'int' = 6
    ARRAY_CUSTOM1: 'int' = 7
    ARRAY_CUSTOM2: 'int' = 8
    ARRAY_CUSTOM3: 'int' = 9
    ARRAY_BONES: 'int' = 10
    ARRAY_WEIGHTS: 'int' = 11
    ARRAY_INDEX: 'int' = 12
    ARRAY_MAX: 'int' = 13




class Mesh__ArrayCustomFormat(Enum):

    ARRAY_CUSTOM_RGBA8_UNORM: 'int' = 0
    ARRAY_CUSTOM_RGBA8_SNORM: 'int' = 1
    ARRAY_CUSTOM_RG_HALF: 'int' = 2
    ARRAY_CUSTOM_RGBA_HALF: 'int' = 3
    ARRAY_CUSTOM_R_FLOAT: 'int' = 4
    ARRAY_CUSTOM_RG_FLOAT: 'int' = 5
    ARRAY_CUSTOM_RGB_FLOAT: 'int' = 6
    ARRAY_CUSTOM_RGBA_FLOAT: 'int' = 7
    ARRAY_CUSTOM_MAX: 'int' = 8




class Mesh__ArrayFormat(Enum):

    ARRAY_FORMAT_VERTEX: 'int' = 1
    ARRAY_FORMAT_NORMAL: 'int' = 2
    ARRAY_FORMAT_TANGENT: 'int' = 4
    ARRAY_FORMAT_COLOR: 'int' = 8
    ARRAY_FORMAT_TEX_UV: 'int' = 16
    ARRAY_FORMAT_TEX_UV2: 'int' = 32
    ARRAY_FORMAT_CUSTOM0: 'int' = 64
    ARRAY_FORMAT_CUSTOM1: 'int' = 128
    ARRAY_FORMAT_CUSTOM2: 'int' = 256
    ARRAY_FORMAT_CUSTOM3: 'int' = 512
    ARRAY_FORMAT_BONES: 'int' = 1024
    ARRAY_FORMAT_WEIGHTS: 'int' = 2048
    ARRAY_FORMAT_INDEX: 'int' = 4096
    ARRAY_FORMAT_BLEND_SHAPE_MASK: 'int' = 7
    ARRAY_FORMAT_CUSTOM_BASE: 'int' = 13
    ARRAY_FORMAT_CUSTOM_BITS: 'int' = 3
    ARRAY_FORMAT_CUSTOM0_SHIFT: 'int' = 13
    ARRAY_FORMAT_CUSTOM1_SHIFT: 'int' = 16
    ARRAY_FORMAT_CUSTOM2_SHIFT: 'int' = 19
    ARRAY_FORMAT_CUSTOM3_SHIFT: 'int' = 22
    ARRAY_FORMAT_CUSTOM_MASK: 'int' = 7
    ARRAY_COMPRESS_FLAGS_BASE: 'int' = 25
    ARRAY_FLAG_USE_2D_VERTICES: 'int' = 33554432
    ARRAY_FLAG_USE_DYNAMIC_UPDATE: 'int' = 67108864
    ARRAY_FLAG_USE_8_BONE_WEIGHTS: 'int' = 134217728
    ARRAY_FLAG_USES_EMPTY_VERTEX_ARRAY: 'int' = 268435456
    ARRAY_FLAG_COMPRESS_ATTRIBUTES: 'int' = 536870912




class Mesh__BlendShapeMode(Enum):

    BLEND_SHAPE_MODE_NORMALIZED: 'int' = 0
    BLEND_SHAPE_MODE_RELATIVE: 'int' = 1




class MeshConvexDecompositionSettings__Mode(Enum):

    CONVEX_DECOMPOSITION_MODE_VOXEL: 'int' = 0
    CONVEX_DECOMPOSITION_MODE_TETRAHEDRON: 'int' = 1




class MultiMesh__TransformFormat(Enum):

    TRANSFORM_2D: 'int' = 0
    TRANSFORM_3D: 'int' = 1




class MultiMesh__PhysicsInterpolationQuality(Enum):

    INTERP_QUALITY_FAST: 'int' = 0
    INTERP_QUALITY_HIGH: 'int' = 1




class MultiplayerAPI__RPCMode(Enum):

    RPC_MODE_DISABLED: 'int' = 0
    RPC_MODE_ANY_PEER: 'int' = 1
    RPC_MODE_AUTHORITY: 'int' = 2




class MultiplayerPeer__ConnectionStatus(Enum):

    CONNECTION_DISCONNECTED: 'int' = 0
    CONNECTION_CONNECTING: 'int' = 1
    CONNECTION_CONNECTED: 'int' = 2




class MultiplayerPeer__TransferMode(Enum):

    TRANSFER_MODE_UNRELIABLE: 'int' = 0
    TRANSFER_MODE_UNRELIABLE_ORDERED: 'int' = 1
    TRANSFER_MODE_RELIABLE: 'int' = 2




class MultiplayerSynchronizer__VisibilityUpdateMode(Enum):

    VISIBILITY_PROCESS_IDLE: 'int' = 0
    VISIBILITY_PROCESS_PHYSICS: 'int' = 1
    VISIBILITY_PROCESS_NONE: 'int' = 2




class NativeMenu__Feature(Enum):

    FEATURE_GLOBAL_MENU: 'int' = 0
    FEATURE_POPUP_MENU: 'int' = 1
    FEATURE_OPEN_CLOSE_CALLBACK: 'int' = 2
    FEATURE_HOVER_CALLBACK: 'int' = 3
    FEATURE_KEY_CALLBACK: 'int' = 4




class NativeMenu__SystemMenus(Enum):

    INVALID_MENU_ID: 'int' = 0
    MAIN_MENU_ID: 'int' = 1
    APPLICATION_MENU_ID: 'int' = 2
    WINDOW_MENU_ID: 'int' = 3
    HELP_MENU_ID: 'int' = 4
    DOCK_MENU_ID: 'int' = 5




class NavigationMesh__SamplePartitionType(Enum):

    SAMPLE_PARTITION_WATERSHED: 'int' = 0
    SAMPLE_PARTITION_MONOTONE: 'int' = 1
    SAMPLE_PARTITION_LAYERS: 'int' = 2
    SAMPLE_PARTITION_MAX: 'int' = 3




class NavigationMesh__ParsedGeometryType(Enum):

    PARSED_GEOMETRY_MESH_INSTANCES: 'int' = 0
    PARSED_GEOMETRY_STATIC_COLLIDERS: 'int' = 1
    PARSED_GEOMETRY_BOTH: 'int' = 2
    PARSED_GEOMETRY_MAX: 'int' = 3




class NavigationMesh__SourceGeometryMode(Enum):

    SOURCE_GEOMETRY_ROOT_NODE_CHILDREN: 'int' = 0
    SOURCE_GEOMETRY_GROUPS_WITH_CHILDREN: 'int' = 1
    SOURCE_GEOMETRY_GROUPS_EXPLICIT: 'int' = 2
    SOURCE_GEOMETRY_MAX: 'int' = 3




class NavigationPathQueryParameters2D__PathfindingAlgorithm(Enum):

    PATHFINDING_ALGORITHM_ASTAR: 'int' = 0




class NavigationPathQueryParameters2D__PathPostProcessing(Enum):

    PATH_POSTPROCESSING_CORRIDORFUNNEL: 'int' = 0
    PATH_POSTPROCESSING_EDGECENTERED: 'int' = 1
    PATH_POSTPROCESSING_NONE: 'int' = 2




class NavigationPathQueryParameters2D__PathMetadataFlags(Enum):

    PATH_METADATA_INCLUDE_NONE: 'int' = 0
    PATH_METADATA_INCLUDE_TYPES: 'int' = 1
    PATH_METADATA_INCLUDE_RIDS: 'int' = 2
    PATH_METADATA_INCLUDE_OWNERS: 'int' = 4
    PATH_METADATA_INCLUDE_ALL: 'int' = 7




class NavigationPathQueryParameters3D__PathfindingAlgorithm(Enum):

    PATHFINDING_ALGORITHM_ASTAR: 'int' = 0




class NavigationPathQueryParameters3D__PathPostProcessing(Enum):

    PATH_POSTPROCESSING_CORRIDORFUNNEL: 'int' = 0
    PATH_POSTPROCESSING_EDGECENTERED: 'int' = 1
    PATH_POSTPROCESSING_NONE: 'int' = 2




class NavigationPathQueryParameters3D__PathMetadataFlags(Enum):

    PATH_METADATA_INCLUDE_NONE: 'int' = 0
    PATH_METADATA_INCLUDE_TYPES: 'int' = 1
    PATH_METADATA_INCLUDE_RIDS: 'int' = 2
    PATH_METADATA_INCLUDE_OWNERS: 'int' = 4
    PATH_METADATA_INCLUDE_ALL: 'int' = 7




class NavigationPathQueryResult2D__PathSegmentType(Enum):

    PATH_SEGMENT_TYPE_REGION: 'int' = 0
    PATH_SEGMENT_TYPE_LINK: 'int' = 1




class NavigationPathQueryResult3D__PathSegmentType(Enum):

    PATH_SEGMENT_TYPE_REGION: 'int' = 0
    PATH_SEGMENT_TYPE_LINK: 'int' = 1




class NavigationPolygon__SamplePartitionType(Enum):

    SAMPLE_PARTITION_CONVEX_PARTITION: 'int' = 0
    SAMPLE_PARTITION_TRIANGULATE: 'int' = 1
    SAMPLE_PARTITION_MAX: 'int' = 2




class NavigationPolygon__ParsedGeometryType(Enum):

    PARSED_GEOMETRY_MESH_INSTANCES: 'int' = 0
    PARSED_GEOMETRY_STATIC_COLLIDERS: 'int' = 1
    PARSED_GEOMETRY_BOTH: 'int' = 2
    PARSED_GEOMETRY_MAX: 'int' = 3




class NavigationPolygon__SourceGeometryMode(Enum):

    SOURCE_GEOMETRY_ROOT_NODE_CHILDREN: 'int' = 0
    SOURCE_GEOMETRY_GROUPS_WITH_CHILDREN: 'int' = 1
    SOURCE_GEOMETRY_GROUPS_EXPLICIT: 'int' = 2
    SOURCE_GEOMETRY_MAX: 'int' = 3




class NavigationServer3D__ProcessInfo(Enum):

    INFO_ACTIVE_MAPS: 'int' = 0
    INFO_REGION_COUNT: 'int' = 1
    INFO_AGENT_COUNT: 'int' = 2
    INFO_LINK_COUNT: 'int' = 3
    INFO_POLYGON_COUNT: 'int' = 4
    INFO_EDGE_COUNT: 'int' = 5
    INFO_EDGE_MERGE_COUNT: 'int' = 6
    INFO_EDGE_CONNECTION_COUNT: 'int' = 7
    INFO_EDGE_FREE_COUNT: 'int' = 8
    INFO_OBSTACLE_COUNT: 'int' = 9




class NinePatchRect__AxisStretchMode(Enum):

    AXIS_STRETCH_MODE_STRETCH: 'int' = 0
    AXIS_STRETCH_MODE_TILE: 'int' = 1
    AXIS_STRETCH_MODE_TILE_FIT: 'int' = 2




class Node__ProcessMode(Enum):

    PROCESS_MODE_INHERIT: 'int' = 0
    PROCESS_MODE_PAUSABLE: 'int' = 1
    PROCESS_MODE_WHEN_PAUSED: 'int' = 2
    PROCESS_MODE_ALWAYS: 'int' = 3
    PROCESS_MODE_DISABLED: 'int' = 4




class Node__ProcessThreadGroup(Enum):

    PROCESS_THREAD_GROUP_INHERIT: 'int' = 0
    PROCESS_THREAD_GROUP_MAIN_THREAD: 'int' = 1
    PROCESS_THREAD_GROUP_SUB_THREAD: 'int' = 2




class Node__ProcessThreadMessages(Enum):

    FLAG_PROCESS_THREAD_MESSAGES: 'int' = 1
    FLAG_PROCESS_THREAD_MESSAGES_PHYSICS: 'int' = 2
    FLAG_PROCESS_THREAD_MESSAGES_ALL: 'int' = 3




class Node__PhysicsInterpolationMode(Enum):

    PHYSICS_INTERPOLATION_MODE_INHERIT: 'int' = 0
    PHYSICS_INTERPOLATION_MODE_ON: 'int' = 1
    PHYSICS_INTERPOLATION_MODE_OFF: 'int' = 2




class Node__DuplicateFlags(Enum):

    DUPLICATE_SIGNALS: 'int' = 1
    DUPLICATE_GROUPS: 'int' = 2
    DUPLICATE_SCRIPTS: 'int' = 4
    DUPLICATE_USE_INSTANTIATION: 'int' = 8




class Node__InternalMode(Enum):

    INTERNAL_MODE_DISABLED: 'int' = 0
    INTERNAL_MODE_FRONT: 'int' = 1
    INTERNAL_MODE_BACK: 'int' = 2




class Node__AutoTranslateMode(Enum):

    AUTO_TRANSLATE_MODE_INHERIT: 'int' = 0
    AUTO_TRANSLATE_MODE_ALWAYS: 'int' = 1
    AUTO_TRANSLATE_MODE_DISABLED: 'int' = 2




class Node3D__RotationEditMode(Enum):

    ROTATION_EDIT_MODE_EULER: 'int' = 0
    ROTATION_EDIT_MODE_QUATERNION: 'int' = 1
    ROTATION_EDIT_MODE_BASIS: 'int' = 2




class OS__RenderingDriver(Enum):

    RENDERING_DRIVER_VULKAN: 'int' = 0
    RENDERING_DRIVER_OPENGL3: 'int' = 1
    RENDERING_DRIVER_D3D12: 'int' = 2
    RENDERING_DRIVER_METAL: 'int' = 3




class OS__SystemDir(Enum):

    SYSTEM_DIR_DESKTOP: 'int' = 0
    SYSTEM_DIR_DCIM: 'int' = 1
    SYSTEM_DIR_DOCUMENTS: 'int' = 2
    SYSTEM_DIR_DOWNLOADS: 'int' = 3
    SYSTEM_DIR_MOVIES: 'int' = 4
    SYSTEM_DIR_MUSIC: 'int' = 5
    SYSTEM_DIR_PICTURES: 'int' = 6
    SYSTEM_DIR_RINGTONES: 'int' = 7




class OS__StdHandleType(Enum):

    STD_HANDLE_INVALID: 'int' = 0
    STD_HANDLE_CONSOLE: 'int' = 1
    STD_HANDLE_FILE: 'int' = 2
    STD_HANDLE_PIPE: 'int' = 3
    STD_HANDLE_UNKNOWN: 'int' = 4




class Object__ConnectFlags(Enum):

    CONNECT_DEFERRED: 'int' = 1
    CONNECT_PERSIST: 'int' = 2
    CONNECT_ONE_SHOT: 'int' = 4
    CONNECT_REFERENCE_COUNTED: 'int' = 8




class OccluderPolygon2D__CullMode(Enum):

    CULL_DISABLED: 'int' = 0
    CULL_CLOCKWISE: 'int' = 1
    CULL_COUNTER_CLOCKWISE: 'int' = 2




class OmniLight3D__ShadowMode(Enum):

    SHADOW_DUAL_PARABOLOID: 'int' = 0
    SHADOW_CUBE: 'int' = 1




class OpenXRAPIExtension__OpenXRAlphaBlendModeSupport(Enum):

    OPENXR_ALPHA_BLEND_MODE_SUPPORT_NONE: 'int' = 0
    OPENXR_ALPHA_BLEND_MODE_SUPPORT_REAL: 'int' = 1
    OPENXR_ALPHA_BLEND_MODE_SUPPORT_EMULATING: 'int' = 2




class OpenXRAction__ActionType(Enum):

    OPENXR_ACTION_BOOL: 'int' = 0
    OPENXR_ACTION_FLOAT: 'int' = 1
    OPENXR_ACTION_VECTOR2: 'int' = 2
    OPENXR_ACTION_POSE: 'int' = 3




class OpenXRHand__Hands(Enum):

    HAND_LEFT: 'int' = 0
    HAND_RIGHT: 'int' = 1
    HAND_MAX: 'int' = 2




class OpenXRHand__MotionRange(Enum):

    MOTION_RANGE_UNOBSTRUCTED: 'int' = 0
    MOTION_RANGE_CONFORM_TO_CONTROLLER: 'int' = 1
    MOTION_RANGE_MAX: 'int' = 2




class OpenXRHand__SkeletonRig(Enum):

    SKELETON_RIG_OPENXR: 'int' = 0
    SKELETON_RIG_HUMANOID: 'int' = 1
    SKELETON_RIG_MAX: 'int' = 2




class OpenXRHand__BoneUpdate(Enum):

    BONE_UPDATE_FULL: 'int' = 0
    BONE_UPDATE_ROTATION_ONLY: 'int' = 1
    BONE_UPDATE_MAX: 'int' = 2




class OpenXRInterface__Hand(Enum):

    HAND_LEFT: 'int' = 0
    HAND_RIGHT: 'int' = 1
    HAND_MAX: 'int' = 2




class OpenXRInterface__HandMotionRange(Enum):

    HAND_MOTION_RANGE_UNOBSTRUCTED: 'int' = 0
    HAND_MOTION_RANGE_CONFORM_TO_CONTROLLER: 'int' = 1
    HAND_MOTION_RANGE_MAX: 'int' = 2




class OpenXRInterface__HandTrackedSource(Enum):

    HAND_TRACKED_SOURCE_UNKNOWN: 'int' = 0
    HAND_TRACKED_SOURCE_UNOBSTRUCTED: 'int' = 1
    HAND_TRACKED_SOURCE_CONTROLLER: 'int' = 2
    HAND_TRACKED_SOURCE_MAX: 'int' = 3




class OpenXRInterface__HandJoints(Enum):

    HAND_JOINT_PALM: 'int' = 0
    HAND_JOINT_WRIST: 'int' = 1
    HAND_JOINT_THUMB_METACARPAL: 'int' = 2
    HAND_JOINT_THUMB_PROXIMAL: 'int' = 3
    HAND_JOINT_THUMB_DISTAL: 'int' = 4
    HAND_JOINT_THUMB_TIP: 'int' = 5
    HAND_JOINT_INDEX_METACARPAL: 'int' = 6
    HAND_JOINT_INDEX_PROXIMAL: 'int' = 7
    HAND_JOINT_INDEX_INTERMEDIATE: 'int' = 8
    HAND_JOINT_INDEX_DISTAL: 'int' = 9
    HAND_JOINT_INDEX_TIP: 'int' = 10
    HAND_JOINT_MIDDLE_METACARPAL: 'int' = 11
    HAND_JOINT_MIDDLE_PROXIMAL: 'int' = 12
    HAND_JOINT_MIDDLE_INTERMEDIATE: 'int' = 13
    HAND_JOINT_MIDDLE_DISTAL: 'int' = 14
    HAND_JOINT_MIDDLE_TIP: 'int' = 15
    HAND_JOINT_RING_METACARPAL: 'int' = 16
    HAND_JOINT_RING_PROXIMAL: 'int' = 17
    HAND_JOINT_RING_INTERMEDIATE: 'int' = 18
    HAND_JOINT_RING_DISTAL: 'int' = 19
    HAND_JOINT_RING_TIP: 'int' = 20
    HAND_JOINT_LITTLE_METACARPAL: 'int' = 21
    HAND_JOINT_LITTLE_PROXIMAL: 'int' = 22
    HAND_JOINT_LITTLE_INTERMEDIATE: 'int' = 23
    HAND_JOINT_LITTLE_DISTAL: 'int' = 24
    HAND_JOINT_LITTLE_TIP: 'int' = 25
    HAND_JOINT_MAX: 'int' = 26




class OpenXRInterface__HandJointFlags(Enum):

    HAND_JOINT_NONE: 'int' = 0
    HAND_JOINT_ORIENTATION_VALID: 'int' = 1
    HAND_JOINT_ORIENTATION_TRACKED: 'int' = 2
    HAND_JOINT_POSITION_VALID: 'int' = 4
    HAND_JOINT_POSITION_TRACKED: 'int' = 8
    HAND_JOINT_LINEAR_VELOCITY_VALID: 'int' = 16
    HAND_JOINT_ANGULAR_VELOCITY_VALID: 'int' = 32




class PackedScene__GenEditState(Enum):

    GEN_EDIT_STATE_DISABLED: 'int' = 0
    GEN_EDIT_STATE_INSTANCE: 'int' = 1
    GEN_EDIT_STATE_MAIN: 'int' = 2
    GEN_EDIT_STATE_MAIN_INHERITED: 'int' = 3




class PacketPeerDTLS__Status(Enum):

    STATUS_DISCONNECTED: 'int' = 0
    STATUS_HANDSHAKING: 'int' = 1
    STATUS_CONNECTED: 'int' = 2
    STATUS_ERROR: 'int' = 3
    STATUS_ERROR_HOSTNAME_MISMATCH: 'int' = 4




class ParticleProcessMaterial__Parameter(Enum):

    PARAM_INITIAL_LINEAR_VELOCITY: 'int' = 0
    PARAM_ANGULAR_VELOCITY: 'int' = 1
    PARAM_ORBIT_VELOCITY: 'int' = 2
    PARAM_LINEAR_ACCEL: 'int' = 3
    PARAM_RADIAL_ACCEL: 'int' = 4
    PARAM_TANGENTIAL_ACCEL: 'int' = 5
    PARAM_DAMPING: 'int' = 6
    PARAM_ANGLE: 'int' = 7
    PARAM_SCALE: 'int' = 8
    PARAM_HUE_VARIATION: 'int' = 9
    PARAM_ANIM_SPEED: 'int' = 10
    PARAM_ANIM_OFFSET: 'int' = 11
    PARAM_RADIAL_VELOCITY: 'int' = 15
    PARAM_DIRECTIONAL_VELOCITY: 'int' = 16
    PARAM_SCALE_OVER_VELOCITY: 'int' = 17
    PARAM_MAX: 'int' = 18
    PARAM_TURB_VEL_INFLUENCE: 'int' = 13
    PARAM_TURB_INIT_DISPLACEMENT: 'int' = 14
    PARAM_TURB_INFLUENCE_OVER_LIFE: 'int' = 12




class ParticleProcessMaterial__ParticleFlags(Enum):

    PARTICLE_FLAG_ALIGN_Y_TO_VELOCITY: 'int' = 0
    PARTICLE_FLAG_ROTATE_Y: 'int' = 1
    PARTICLE_FLAG_DISABLE_Z: 'int' = 2
    PARTICLE_FLAG_DAMPING_AS_FRICTION: 'int' = 3
    PARTICLE_FLAG_MAX: 'int' = 4




class ParticleProcessMaterial__EmissionShape(Enum):

    EMISSION_SHAPE_POINT: 'int' = 0
    EMISSION_SHAPE_SPHERE: 'int' = 1
    EMISSION_SHAPE_SPHERE_SURFACE: 'int' = 2
    EMISSION_SHAPE_BOX: 'int' = 3
    EMISSION_SHAPE_POINTS: 'int' = 4
    EMISSION_SHAPE_DIRECTED_POINTS: 'int' = 5
    EMISSION_SHAPE_RING: 'int' = 6
    EMISSION_SHAPE_MAX: 'int' = 7




class ParticleProcessMaterial__SubEmitterMode(Enum):

    SUB_EMITTER_DISABLED: 'int' = 0
    SUB_EMITTER_CONSTANT: 'int' = 1
    SUB_EMITTER_AT_END: 'int' = 2
    SUB_EMITTER_AT_COLLISION: 'int' = 3
    SUB_EMITTER_AT_START: 'int' = 4
    SUB_EMITTER_MAX: 'int' = 5




class ParticleProcessMaterial__CollisionMode(Enum):

    COLLISION_DISABLED: 'int' = 0
    COLLISION_RIGID: 'int' = 1
    COLLISION_HIDE_ON_CONTACT: 'int' = 2
    COLLISION_MAX: 'int' = 3




class PathFollow3D__RotationMode(Enum):

    ROTATION_NONE: 'int' = 0
    ROTATION_Y: 'int' = 1
    ROTATION_XY: 'int' = 2
    ROTATION_XYZ: 'int' = 3
    ROTATION_ORIENTED: 'int' = 4




class Performance__Monitor(Enum):

    TIME_FPS: 'int' = 0
    TIME_PROCESS: 'int' = 1
    TIME_PHYSICS_PROCESS: 'int' = 2
    TIME_NAVIGATION_PROCESS: 'int' = 3
    MEMORY_STATIC: 'int' = 4
    MEMORY_STATIC_MAX: 'int' = 5
    MEMORY_MESSAGE_BUFFER_MAX: 'int' = 6
    OBJECT_COUNT: 'int' = 7
    OBJECT_RESOURCE_COUNT: 'int' = 8
    OBJECT_NODE_COUNT: 'int' = 9
    OBJECT_ORPHAN_NODE_COUNT: 'int' = 10
    RENDER_TOTAL_OBJECTS_IN_FRAME: 'int' = 11
    RENDER_TOTAL_PRIMITIVES_IN_FRAME: 'int' = 12
    RENDER_TOTAL_DRAW_CALLS_IN_FRAME: 'int' = 13
    RENDER_VIDEO_MEM_USED: 'int' = 14
    RENDER_TEXTURE_MEM_USED: 'int' = 15
    RENDER_BUFFER_MEM_USED: 'int' = 16
    PHYSICS_2D_ACTIVE_OBJECTS: 'int' = 17
    PHYSICS_2D_COLLISION_PAIRS: 'int' = 18
    PHYSICS_2D_ISLAND_COUNT: 'int' = 19
    PHYSICS_3D_ACTIVE_OBJECTS: 'int' = 20
    PHYSICS_3D_COLLISION_PAIRS: 'int' = 21
    PHYSICS_3D_ISLAND_COUNT: 'int' = 22
    AUDIO_OUTPUT_LATENCY: 'int' = 23
    NAVIGATION_ACTIVE_MAPS: 'int' = 24
    NAVIGATION_REGION_COUNT: 'int' = 25
    NAVIGATION_AGENT_COUNT: 'int' = 26
    NAVIGATION_LINK_COUNT: 'int' = 27
    NAVIGATION_POLYGON_COUNT: 'int' = 28
    NAVIGATION_EDGE_COUNT: 'int' = 29
    NAVIGATION_EDGE_MERGE_COUNT: 'int' = 30
    NAVIGATION_EDGE_CONNECTION_COUNT: 'int' = 31
    NAVIGATION_EDGE_FREE_COUNT: 'int' = 32
    NAVIGATION_OBSTACLE_COUNT: 'int' = 33
    PIPELINE_COMPILATIONS_CANVAS: 'int' = 34
    PIPELINE_COMPILATIONS_MESH: 'int' = 35
    PIPELINE_COMPILATIONS_SURFACE: 'int' = 36
    PIPELINE_COMPILATIONS_DRAW: 'int' = 37
    PIPELINE_COMPILATIONS_SPECIALIZATION: 'int' = 38
    MONITOR_MAX: 'int' = 39




class PhysicalBone3D__DampMode(Enum):

    DAMP_MODE_COMBINE: 'int' = 0
    DAMP_MODE_REPLACE: 'int' = 1




class PhysicalBone3D__JointType(Enum):

    JOINT_TYPE_NONE: 'int' = 0
    JOINT_TYPE_PIN: 'int' = 1
    JOINT_TYPE_CONE: 'int' = 2
    JOINT_TYPE_HINGE: 'int' = 3
    JOINT_TYPE_SLIDER: 'int' = 4
    JOINT_TYPE_6DOF: 'int' = 5




class PhysicsServer2D__SpaceParameter(Enum):

    SPACE_PARAM_CONTACT_RECYCLE_RADIUS: 'int' = 0
    SPACE_PARAM_CONTACT_MAX_SEPARATION: 'int' = 1
    SPACE_PARAM_CONTACT_MAX_ALLOWED_PENETRATION: 'int' = 2
    SPACE_PARAM_CONTACT_DEFAULT_BIAS: 'int' = 3
    SPACE_PARAM_BODY_LINEAR_VELOCITY_SLEEP_THRESHOLD: 'int' = 4
    SPACE_PARAM_BODY_ANGULAR_VELOCITY_SLEEP_THRESHOLD: 'int' = 5
    SPACE_PARAM_BODY_TIME_TO_SLEEP: 'int' = 6
    SPACE_PARAM_CONSTRAINT_DEFAULT_BIAS: 'int' = 7
    SPACE_PARAM_SOLVER_ITERATIONS: 'int' = 8




class PhysicsServer2D__ShapeType(Enum):

    SHAPE_WORLD_BOUNDARY: 'int' = 0
    SHAPE_SEPARATION_RAY: 'int' = 1
    SHAPE_SEGMENT: 'int' = 2
    SHAPE_CIRCLE: 'int' = 3
    SHAPE_RECTANGLE: 'int' = 4
    SHAPE_CAPSULE: 'int' = 5
    SHAPE_CONVEX_POLYGON: 'int' = 6
    SHAPE_CONCAVE_POLYGON: 'int' = 7
    SHAPE_CUSTOM: 'int' = 8




class PhysicsServer2D__AreaParameter(Enum):

    AREA_PARAM_GRAVITY_OVERRIDE_MODE: 'int' = 0
    AREA_PARAM_GRAVITY: 'int' = 1
    AREA_PARAM_GRAVITY_VECTOR: 'int' = 2
    AREA_PARAM_GRAVITY_IS_POINT: 'int' = 3
    AREA_PARAM_GRAVITY_POINT_UNIT_DISTANCE: 'int' = 4
    AREA_PARAM_LINEAR_DAMP_OVERRIDE_MODE: 'int' = 5
    AREA_PARAM_LINEAR_DAMP: 'int' = 6
    AREA_PARAM_ANGULAR_DAMP_OVERRIDE_MODE: 'int' = 7
    AREA_PARAM_ANGULAR_DAMP: 'int' = 8
    AREA_PARAM_PRIORITY: 'int' = 9




class PhysicsServer2D__AreaSpaceOverrideMode(Enum):

    AREA_SPACE_OVERRIDE_DISABLED: 'int' = 0
    AREA_SPACE_OVERRIDE_COMBINE: 'int' = 1
    AREA_SPACE_OVERRIDE_COMBINE_REPLACE: 'int' = 2
    AREA_SPACE_OVERRIDE_REPLACE: 'int' = 3
    AREA_SPACE_OVERRIDE_REPLACE_COMBINE: 'int' = 4




class PhysicsServer2D__BodyMode(Enum):

    BODY_MODE_STATIC: 'int' = 0
    BODY_MODE_KINEMATIC: 'int' = 1
    BODY_MODE_RIGID: 'int' = 2
    BODY_MODE_RIGID_LINEAR: 'int' = 3




class PhysicsServer2D__BodyParameter(Enum):

    BODY_PARAM_BOUNCE: 'int' = 0
    BODY_PARAM_FRICTION: 'int' = 1
    BODY_PARAM_MASS: 'int' = 2
    BODY_PARAM_INERTIA: 'int' = 3
    BODY_PARAM_CENTER_OF_MASS: 'int' = 4
    BODY_PARAM_GRAVITY_SCALE: 'int' = 5
    BODY_PARAM_LINEAR_DAMP_MODE: 'int' = 6
    BODY_PARAM_ANGULAR_DAMP_MODE: 'int' = 7
    BODY_PARAM_LINEAR_DAMP: 'int' = 8
    BODY_PARAM_ANGULAR_DAMP: 'int' = 9
    BODY_PARAM_MAX: 'int' = 10




class PhysicsServer2D__BodyDampMode(Enum):

    BODY_DAMP_MODE_COMBINE: 'int' = 0
    BODY_DAMP_MODE_REPLACE: 'int' = 1




class PhysicsServer2D__BodyState(Enum):

    BODY_STATE_TRANSFORM: 'int' = 0
    BODY_STATE_LINEAR_VELOCITY: 'int' = 1
    BODY_STATE_ANGULAR_VELOCITY: 'int' = 2
    BODY_STATE_SLEEPING: 'int' = 3
    BODY_STATE_CAN_SLEEP: 'int' = 4




class PhysicsServer2D__JointType(Enum):

    JOINT_TYPE_PIN: 'int' = 0
    JOINT_TYPE_GROOVE: 'int' = 1
    JOINT_TYPE_DAMPED_SPRING: 'int' = 2
    JOINT_TYPE_MAX: 'int' = 3




class PhysicsServer2D__JointParam(Enum):

    JOINT_PARAM_BIAS: 'int' = 0
    JOINT_PARAM_MAX_BIAS: 'int' = 1
    JOINT_PARAM_MAX_FORCE: 'int' = 2




class PhysicsServer2D__PinJointParam(Enum):

    PIN_JOINT_SOFTNESS: 'int' = 0
    PIN_JOINT_LIMIT_UPPER: 'int' = 1
    PIN_JOINT_LIMIT_LOWER: 'int' = 2
    PIN_JOINT_MOTOR_TARGET_VELOCITY: 'int' = 3




class PhysicsServer2D__PinJointFlag(Enum):

    PIN_JOINT_FLAG_ANGULAR_LIMIT_ENABLED: 'int' = 0
    PIN_JOINT_FLAG_MOTOR_ENABLED: 'int' = 1




class PhysicsServer2D__DampedSpringParam(Enum):

    DAMPED_SPRING_REST_LENGTH: 'int' = 0
    DAMPED_SPRING_STIFFNESS: 'int' = 1
    DAMPED_SPRING_DAMPING: 'int' = 2




class PhysicsServer2D__CCDMode(Enum):

    CCD_MODE_DISABLED: 'int' = 0
    CCD_MODE_CAST_RAY: 'int' = 1
    CCD_MODE_CAST_SHAPE: 'int' = 2




class PhysicsServer2D__AreaBodyStatus(Enum):

    AREA_BODY_ADDED: 'int' = 0
    AREA_BODY_REMOVED: 'int' = 1




class PhysicsServer2D__ProcessInfo(Enum):

    INFO_ACTIVE_OBJECTS: 'int' = 0
    INFO_COLLISION_PAIRS: 'int' = 1
    INFO_ISLAND_COUNT: 'int' = 2




class PhysicsServer3D__JointType(Enum):

    JOINT_TYPE_PIN: 'int' = 0
    JOINT_TYPE_HINGE: 'int' = 1
    JOINT_TYPE_SLIDER: 'int' = 2
    JOINT_TYPE_CONE_TWIST: 'int' = 3
    JOINT_TYPE_6DOF: 'int' = 4
    JOINT_TYPE_MAX: 'int' = 5




class PhysicsServer3D__PinJointParam(Enum):

    PIN_JOINT_BIAS: 'int' = 0
    PIN_JOINT_DAMPING: 'int' = 1
    PIN_JOINT_IMPULSE_CLAMP: 'int' = 2




class PhysicsServer3D__HingeJointParam(Enum):

    HINGE_JOINT_BIAS: 'int' = 0
    HINGE_JOINT_LIMIT_UPPER: 'int' = 1
    HINGE_JOINT_LIMIT_LOWER: 'int' = 2
    HINGE_JOINT_LIMIT_BIAS: 'int' = 3
    HINGE_JOINT_LIMIT_SOFTNESS: 'int' = 4
    HINGE_JOINT_LIMIT_RELAXATION: 'int' = 5
    HINGE_JOINT_MOTOR_TARGET_VELOCITY: 'int' = 6
    HINGE_JOINT_MOTOR_MAX_IMPULSE: 'int' = 7




class PhysicsServer3D__HingeJointFlag(Enum):

    HINGE_JOINT_FLAG_USE_LIMIT: 'int' = 0
    HINGE_JOINT_FLAG_ENABLE_MOTOR: 'int' = 1




class PhysicsServer3D__SliderJointParam(Enum):

    SLIDER_JOINT_LINEAR_LIMIT_UPPER: 'int' = 0
    SLIDER_JOINT_LINEAR_LIMIT_LOWER: 'int' = 1
    SLIDER_JOINT_LINEAR_LIMIT_SOFTNESS: 'int' = 2
    SLIDER_JOINT_LINEAR_LIMIT_RESTITUTION: 'int' = 3
    SLIDER_JOINT_LINEAR_LIMIT_DAMPING: 'int' = 4
    SLIDER_JOINT_LINEAR_MOTION_SOFTNESS: 'int' = 5
    SLIDER_JOINT_LINEAR_MOTION_RESTITUTION: 'int' = 6
    SLIDER_JOINT_LINEAR_MOTION_DAMPING: 'int' = 7
    SLIDER_JOINT_LINEAR_ORTHOGONAL_SOFTNESS: 'int' = 8
    SLIDER_JOINT_LINEAR_ORTHOGONAL_RESTITUTION: 'int' = 9
    SLIDER_JOINT_LINEAR_ORTHOGONAL_DAMPING: 'int' = 10
    SLIDER_JOINT_ANGULAR_LIMIT_UPPER: 'int' = 11
    SLIDER_JOINT_ANGULAR_LIMIT_LOWER: 'int' = 12
    SLIDER_JOINT_ANGULAR_LIMIT_SOFTNESS: 'int' = 13
    SLIDER_JOINT_ANGULAR_LIMIT_RESTITUTION: 'int' = 14
    SLIDER_JOINT_ANGULAR_LIMIT_DAMPING: 'int' = 15
    SLIDER_JOINT_ANGULAR_MOTION_SOFTNESS: 'int' = 16
    SLIDER_JOINT_ANGULAR_MOTION_RESTITUTION: 'int' = 17
    SLIDER_JOINT_ANGULAR_MOTION_DAMPING: 'int' = 18
    SLIDER_JOINT_ANGULAR_ORTHOGONAL_SOFTNESS: 'int' = 19
    SLIDER_JOINT_ANGULAR_ORTHOGONAL_RESTITUTION: 'int' = 20
    SLIDER_JOINT_ANGULAR_ORTHOGONAL_DAMPING: 'int' = 21
    SLIDER_JOINT_MAX: 'int' = 22




class PhysicsServer3D__ConeTwistJointParam(Enum):

    CONE_TWIST_JOINT_SWING_SPAN: 'int' = 0
    CONE_TWIST_JOINT_TWIST_SPAN: 'int' = 1
    CONE_TWIST_JOINT_BIAS: 'int' = 2
    CONE_TWIST_JOINT_SOFTNESS: 'int' = 3
    CONE_TWIST_JOINT_RELAXATION: 'int' = 4




class PhysicsServer3D__G6DOFJointAxisParam(Enum):

    G6DOF_JOINT_LINEAR_LOWER_LIMIT: 'int' = 0
    G6DOF_JOINT_LINEAR_UPPER_LIMIT: 'int' = 1
    G6DOF_JOINT_LINEAR_LIMIT_SOFTNESS: 'int' = 2
    G6DOF_JOINT_LINEAR_RESTITUTION: 'int' = 3
    G6DOF_JOINT_LINEAR_DAMPING: 'int' = 4
    G6DOF_JOINT_LINEAR_MOTOR_TARGET_VELOCITY: 'int' = 5
    G6DOF_JOINT_LINEAR_MOTOR_FORCE_LIMIT: 'int' = 6
    G6DOF_JOINT_LINEAR_SPRING_STIFFNESS: 'int' = 7
    G6DOF_JOINT_LINEAR_SPRING_DAMPING: 'int' = 8
    G6DOF_JOINT_LINEAR_SPRING_EQUILIBRIUM_POINT: 'int' = 9
    G6DOF_JOINT_ANGULAR_LOWER_LIMIT: 'int' = 10
    G6DOF_JOINT_ANGULAR_UPPER_LIMIT: 'int' = 11
    G6DOF_JOINT_ANGULAR_LIMIT_SOFTNESS: 'int' = 12
    G6DOF_JOINT_ANGULAR_DAMPING: 'int' = 13
    G6DOF_JOINT_ANGULAR_RESTITUTION: 'int' = 14
    G6DOF_JOINT_ANGULAR_FORCE_LIMIT: 'int' = 15
    G6DOF_JOINT_ANGULAR_ERP: 'int' = 16
    G6DOF_JOINT_ANGULAR_MOTOR_TARGET_VELOCITY: 'int' = 17
    G6DOF_JOINT_ANGULAR_MOTOR_FORCE_LIMIT: 'int' = 18
    G6DOF_JOINT_ANGULAR_SPRING_STIFFNESS: 'int' = 19
    G6DOF_JOINT_ANGULAR_SPRING_DAMPING: 'int' = 20
    G6DOF_JOINT_ANGULAR_SPRING_EQUILIBRIUM_POINT: 'int' = 21
    G6DOF_JOINT_MAX: 'int' = 22




class PhysicsServer3D__G6DOFJointAxisFlag(Enum):

    G6DOF_JOINT_FLAG_ENABLE_LINEAR_LIMIT: 'int' = 0
    G6DOF_JOINT_FLAG_ENABLE_ANGULAR_LIMIT: 'int' = 1
    G6DOF_JOINT_FLAG_ENABLE_ANGULAR_SPRING: 'int' = 2
    G6DOF_JOINT_FLAG_ENABLE_LINEAR_SPRING: 'int' = 3
    G6DOF_JOINT_FLAG_ENABLE_MOTOR: 'int' = 4
    G6DOF_JOINT_FLAG_ENABLE_LINEAR_MOTOR: 'int' = 5
    G6DOF_JOINT_FLAG_MAX: 'int' = 6




class PhysicsServer3D__ShapeType(Enum):

    SHAPE_WORLD_BOUNDARY: 'int' = 0
    SHAPE_SEPARATION_RAY: 'int' = 1
    SHAPE_SPHERE: 'int' = 2
    SHAPE_BOX: 'int' = 3
    SHAPE_CAPSULE: 'int' = 4
    SHAPE_CYLINDER: 'int' = 5
    SHAPE_CONVEX_POLYGON: 'int' = 6
    SHAPE_CONCAVE_POLYGON: 'int' = 7
    SHAPE_HEIGHTMAP: 'int' = 8
    SHAPE_SOFT_BODY: 'int' = 9
    SHAPE_CUSTOM: 'int' = 10




class PhysicsServer3D__AreaParameter(Enum):

    AREA_PARAM_GRAVITY_OVERRIDE_MODE: 'int' = 0
    AREA_PARAM_GRAVITY: 'int' = 1
    AREA_PARAM_GRAVITY_VECTOR: 'int' = 2
    AREA_PARAM_GRAVITY_IS_POINT: 'int' = 3
    AREA_PARAM_GRAVITY_POINT_UNIT_DISTANCE: 'int' = 4
    AREA_PARAM_LINEAR_DAMP_OVERRIDE_MODE: 'int' = 5
    AREA_PARAM_LINEAR_DAMP: 'int' = 6
    AREA_PARAM_ANGULAR_DAMP_OVERRIDE_MODE: 'int' = 7
    AREA_PARAM_ANGULAR_DAMP: 'int' = 8
    AREA_PARAM_PRIORITY: 'int' = 9
    AREA_PARAM_WIND_FORCE_MAGNITUDE: 'int' = 10
    AREA_PARAM_WIND_SOURCE: 'int' = 11
    AREA_PARAM_WIND_DIRECTION: 'int' = 12
    AREA_PARAM_WIND_ATTENUATION_FACTOR: 'int' = 13




class PhysicsServer3D__AreaSpaceOverrideMode(Enum):

    AREA_SPACE_OVERRIDE_DISABLED: 'int' = 0
    AREA_SPACE_OVERRIDE_COMBINE: 'int' = 1
    AREA_SPACE_OVERRIDE_COMBINE_REPLACE: 'int' = 2
    AREA_SPACE_OVERRIDE_REPLACE: 'int' = 3
    AREA_SPACE_OVERRIDE_REPLACE_COMBINE: 'int' = 4




class PhysicsServer3D__BodyMode(Enum):

    BODY_MODE_STATIC: 'int' = 0
    BODY_MODE_KINEMATIC: 'int' = 1
    BODY_MODE_RIGID: 'int' = 2
    BODY_MODE_RIGID_LINEAR: 'int' = 3




class PhysicsServer3D__BodyParameter(Enum):

    BODY_PARAM_BOUNCE: 'int' = 0
    BODY_PARAM_FRICTION: 'int' = 1
    BODY_PARAM_MASS: 'int' = 2
    BODY_PARAM_INERTIA: 'int' = 3
    BODY_PARAM_CENTER_OF_MASS: 'int' = 4
    BODY_PARAM_GRAVITY_SCALE: 'int' = 5
    BODY_PARAM_LINEAR_DAMP_MODE: 'int' = 6
    BODY_PARAM_ANGULAR_DAMP_MODE: 'int' = 7
    BODY_PARAM_LINEAR_DAMP: 'int' = 8
    BODY_PARAM_ANGULAR_DAMP: 'int' = 9
    BODY_PARAM_MAX: 'int' = 10




class PhysicsServer3D__BodyDampMode(Enum):

    BODY_DAMP_MODE_COMBINE: 'int' = 0
    BODY_DAMP_MODE_REPLACE: 'int' = 1




class PhysicsServer3D__BodyState(Enum):

    BODY_STATE_TRANSFORM: 'int' = 0
    BODY_STATE_LINEAR_VELOCITY: 'int' = 1
    BODY_STATE_ANGULAR_VELOCITY: 'int' = 2
    BODY_STATE_SLEEPING: 'int' = 3
    BODY_STATE_CAN_SLEEP: 'int' = 4




class PhysicsServer3D__AreaBodyStatus(Enum):

    AREA_BODY_ADDED: 'int' = 0
    AREA_BODY_REMOVED: 'int' = 1




class PhysicsServer3D__ProcessInfo(Enum):

    INFO_ACTIVE_OBJECTS: 'int' = 0
    INFO_COLLISION_PAIRS: 'int' = 1
    INFO_ISLAND_COUNT: 'int' = 2




class PhysicsServer3D__SpaceParameter(Enum):

    SPACE_PARAM_CONTACT_RECYCLE_RADIUS: 'int' = 0
    SPACE_PARAM_CONTACT_MAX_SEPARATION: 'int' = 1
    SPACE_PARAM_CONTACT_MAX_ALLOWED_PENETRATION: 'int' = 2
    SPACE_PARAM_CONTACT_DEFAULT_BIAS: 'int' = 3
    SPACE_PARAM_BODY_LINEAR_VELOCITY_SLEEP_THRESHOLD: 'int' = 4
    SPACE_PARAM_BODY_ANGULAR_VELOCITY_SLEEP_THRESHOLD: 'int' = 5
    SPACE_PARAM_BODY_TIME_TO_SLEEP: 'int' = 6
    SPACE_PARAM_SOLVER_ITERATIONS: 'int' = 7




class PhysicsServer3D__BodyAxis(Enum):

    BODY_AXIS_LINEAR_X: 'int' = 1
    BODY_AXIS_LINEAR_Y: 'int' = 2
    BODY_AXIS_LINEAR_Z: 'int' = 4
    BODY_AXIS_ANGULAR_X: 'int' = 8
    BODY_AXIS_ANGULAR_Y: 'int' = 16
    BODY_AXIS_ANGULAR_Z: 'int' = 32




class PinJoint3D__Param(Enum):

    PARAM_BIAS: 'int' = 0
    PARAM_DAMPING: 'int' = 1
    PARAM_IMPULSE_CLAMP: 'int' = 2




class PlaneMesh__Orientation(Enum):

    FACE_X: 'int' = 0
    FACE_Y: 'int' = 1
    FACE_Z: 'int' = 2




class PortableCompressedTexture2D__CompressionMode(Enum):

    COMPRESSION_MODE_LOSSLESS: 'int' = 0
    COMPRESSION_MODE_LOSSY: 'int' = 1
    COMPRESSION_MODE_BASIS_UNIVERSAL: 'int' = 2
    COMPRESSION_MODE_S3TC: 'int' = 3
    COMPRESSION_MODE_ETC2: 'int' = 4
    COMPRESSION_MODE_BPTC: 'int' = 5




class ProgressBar__FillMode(Enum):

    FILL_BEGIN_TO_END: 'int' = 0
    FILL_END_TO_BEGIN: 'int' = 1
    FILL_TOP_TO_BOTTOM: 'int' = 2
    FILL_BOTTOM_TO_TOP: 'int' = 3




class ReflectionProbe__UpdateMode(Enum):

    UPDATE_ONCE: 'int' = 0
    UPDATE_ALWAYS: 'int' = 1




class ReflectionProbe__AmbientMode(Enum):

    AMBIENT_DISABLED: 'int' = 0
    AMBIENT_ENVIRONMENT: 'int' = 1
    AMBIENT_COLOR: 'int' = 2




class RenderingDevice__DeviceType(Enum):

    DEVICE_TYPE_OTHER: 'int' = 0
    DEVICE_TYPE_INTEGRATED_GPU: 'int' = 1
    DEVICE_TYPE_DISCRETE_GPU: 'int' = 2
    DEVICE_TYPE_VIRTUAL_GPU: 'int' = 3
    DEVICE_TYPE_CPU: 'int' = 4
    DEVICE_TYPE_MAX: 'int' = 5




class RenderingDevice__DriverResource(Enum):

    DRIVER_RESOURCE_LOGICAL_DEVICE: 'int' = 0
    DRIVER_RESOURCE_PHYSICAL_DEVICE: 'int' = 1
    DRIVER_RESOURCE_TOPMOST_OBJECT: 'int' = 2
    DRIVER_RESOURCE_COMMAND_QUEUE: 'int' = 3
    DRIVER_RESOURCE_QUEUE_FAMILY: 'int' = 4
    DRIVER_RESOURCE_TEXTURE: 'int' = 5
    DRIVER_RESOURCE_TEXTURE_VIEW: 'int' = 6
    DRIVER_RESOURCE_TEXTURE_DATA_FORMAT: 'int' = 7
    DRIVER_RESOURCE_SAMPLER: 'int' = 8
    DRIVER_RESOURCE_UNIFORM_SET: 'int' = 9
    DRIVER_RESOURCE_BUFFER: 'int' = 10
    DRIVER_RESOURCE_COMPUTE_PIPELINE: 'int' = 11
    DRIVER_RESOURCE_RENDER_PIPELINE: 'int' = 12
    DRIVER_RESOURCE_VULKAN_DEVICE: 'int' = 0
    DRIVER_RESOURCE_VULKAN_PHYSICAL_DEVICE: 'int' = 1
    DRIVER_RESOURCE_VULKAN_INSTANCE: 'int' = 2
    DRIVER_RESOURCE_VULKAN_QUEUE: 'int' = 3
    DRIVER_RESOURCE_VULKAN_QUEUE_FAMILY_INDEX: 'int' = 4
    DRIVER_RESOURCE_VULKAN_IMAGE: 'int' = 5
    DRIVER_RESOURCE_VULKAN_IMAGE_VIEW: 'int' = 6
    DRIVER_RESOURCE_VULKAN_IMAGE_NATIVE_TEXTURE_FORMAT: 'int' = 7
    DRIVER_RESOURCE_VULKAN_SAMPLER: 'int' = 8
    DRIVER_RESOURCE_VULKAN_DESCRIPTOR_SET: 'int' = 9
    DRIVER_RESOURCE_VULKAN_BUFFER: 'int' = 10
    DRIVER_RESOURCE_VULKAN_COMPUTE_PIPELINE: 'int' = 11
    DRIVER_RESOURCE_VULKAN_RENDER_PIPELINE: 'int' = 12




class RenderingDevice__DataFormat(Enum):

    DATA_FORMAT_R4G4_UNORM_PACK8: 'int' = 0
    DATA_FORMAT_R4G4B4A4_UNORM_PACK16: 'int' = 1
    DATA_FORMAT_B4G4R4A4_UNORM_PACK16: 'int' = 2
    DATA_FORMAT_R5G6B5_UNORM_PACK16: 'int' = 3
    DATA_FORMAT_B5G6R5_UNORM_PACK16: 'int' = 4
    DATA_FORMAT_R5G5B5A1_UNORM_PACK16: 'int' = 5
    DATA_FORMAT_B5G5R5A1_UNORM_PACK16: 'int' = 6
    DATA_FORMAT_A1R5G5B5_UNORM_PACK16: 'int' = 7
    DATA_FORMAT_R8_UNORM: 'int' = 8
    DATA_FORMAT_R8_SNORM: 'int' = 9
    DATA_FORMAT_R8_USCALED: 'int' = 10
    DATA_FORMAT_R8_SSCALED: 'int' = 11
    DATA_FORMAT_R8_UINT: 'int' = 12
    DATA_FORMAT_R8_SINT: 'int' = 13
    DATA_FORMAT_R8_SRGB: 'int' = 14
    DATA_FORMAT_R8G8_UNORM: 'int' = 15
    DATA_FORMAT_R8G8_SNORM: 'int' = 16
    DATA_FORMAT_R8G8_USCALED: 'int' = 17
    DATA_FORMAT_R8G8_SSCALED: 'int' = 18
    DATA_FORMAT_R8G8_UINT: 'int' = 19
    DATA_FORMAT_R8G8_SINT: 'int' = 20
    DATA_FORMAT_R8G8_SRGB: 'int' = 21
    DATA_FORMAT_R8G8B8_UNORM: 'int' = 22
    DATA_FORMAT_R8G8B8_SNORM: 'int' = 23
    DATA_FORMAT_R8G8B8_USCALED: 'int' = 24
    DATA_FORMAT_R8G8B8_SSCALED: 'int' = 25
    DATA_FORMAT_R8G8B8_UINT: 'int' = 26
    DATA_FORMAT_R8G8B8_SINT: 'int' = 27
    DATA_FORMAT_R8G8B8_SRGB: 'int' = 28
    DATA_FORMAT_B8G8R8_UNORM: 'int' = 29
    DATA_FORMAT_B8G8R8_SNORM: 'int' = 30
    DATA_FORMAT_B8G8R8_USCALED: 'int' = 31
    DATA_FORMAT_B8G8R8_SSCALED: 'int' = 32
    DATA_FORMAT_B8G8R8_UINT: 'int' = 33
    DATA_FORMAT_B8G8R8_SINT: 'int' = 34
    DATA_FORMAT_B8G8R8_SRGB: 'int' = 35
    DATA_FORMAT_R8G8B8A8_UNORM: 'int' = 36
    DATA_FORMAT_R8G8B8A8_SNORM: 'int' = 37
    DATA_FORMAT_R8G8B8A8_USCALED: 'int' = 38
    DATA_FORMAT_R8G8B8A8_SSCALED: 'int' = 39
    DATA_FORMAT_R8G8B8A8_UINT: 'int' = 40
    DATA_FORMAT_R8G8B8A8_SINT: 'int' = 41
    DATA_FORMAT_R8G8B8A8_SRGB: 'int' = 42
    DATA_FORMAT_B8G8R8A8_UNORM: 'int' = 43
    DATA_FORMAT_B8G8R8A8_SNORM: 'int' = 44
    DATA_FORMAT_B8G8R8A8_USCALED: 'int' = 45
    DATA_FORMAT_B8G8R8A8_SSCALED: 'int' = 46
    DATA_FORMAT_B8G8R8A8_UINT: 'int' = 47
    DATA_FORMAT_B8G8R8A8_SINT: 'int' = 48
    DATA_FORMAT_B8G8R8A8_SRGB: 'int' = 49
    DATA_FORMAT_A8B8G8R8_UNORM_PACK32: 'int' = 50
    DATA_FORMAT_A8B8G8R8_SNORM_PACK32: 'int' = 51
    DATA_FORMAT_A8B8G8R8_USCALED_PACK32: 'int' = 52
    DATA_FORMAT_A8B8G8R8_SSCALED_PACK32: 'int' = 53
    DATA_FORMAT_A8B8G8R8_UINT_PACK32: 'int' = 54
    DATA_FORMAT_A8B8G8R8_SINT_PACK32: 'int' = 55
    DATA_FORMAT_A8B8G8R8_SRGB_PACK32: 'int' = 56
    DATA_FORMAT_A2R10G10B10_UNORM_PACK32: 'int' = 57
    DATA_FORMAT_A2R10G10B10_SNORM_PACK32: 'int' = 58
    DATA_FORMAT_A2R10G10B10_USCALED_PACK32: 'int' = 59
    DATA_FORMAT_A2R10G10B10_SSCALED_PACK32: 'int' = 60
    DATA_FORMAT_A2R10G10B10_UINT_PACK32: 'int' = 61
    DATA_FORMAT_A2R10G10B10_SINT_PACK32: 'int' = 62
    DATA_FORMAT_A2B10G10R10_UNORM_PACK32: 'int' = 63
    DATA_FORMAT_A2B10G10R10_SNORM_PACK32: 'int' = 64
    DATA_FORMAT_A2B10G10R10_USCALED_PACK32: 'int' = 65
    DATA_FORMAT_A2B10G10R10_SSCALED_PACK32: 'int' = 66
    DATA_FORMAT_A2B10G10R10_UINT_PACK32: 'int' = 67
    DATA_FORMAT_A2B10G10R10_SINT_PACK32: 'int' = 68
    DATA_FORMAT_R16_UNORM: 'int' = 69
    DATA_FORMAT_R16_SNORM: 'int' = 70
    DATA_FORMAT_R16_USCALED: 'int' = 71
    DATA_FORMAT_R16_SSCALED: 'int' = 72
    DATA_FORMAT_R16_UINT: 'int' = 73
    DATA_FORMAT_R16_SINT: 'int' = 74
    DATA_FORMAT_R16_SFLOAT: 'int' = 75
    DATA_FORMAT_R16G16_UNORM: 'int' = 76
    DATA_FORMAT_R16G16_SNORM: 'int' = 77
    DATA_FORMAT_R16G16_USCALED: 'int' = 78
    DATA_FORMAT_R16G16_SSCALED: 'int' = 79
    DATA_FORMAT_R16G16_UINT: 'int' = 80
    DATA_FORMAT_R16G16_SINT: 'int' = 81
    DATA_FORMAT_R16G16_SFLOAT: 'int' = 82
    DATA_FORMAT_R16G16B16_UNORM: 'int' = 83
    DATA_FORMAT_R16G16B16_SNORM: 'int' = 84
    DATA_FORMAT_R16G16B16_USCALED: 'int' = 85
    DATA_FORMAT_R16G16B16_SSCALED: 'int' = 86
    DATA_FORMAT_R16G16B16_UINT: 'int' = 87
    DATA_FORMAT_R16G16B16_SINT: 'int' = 88
    DATA_FORMAT_R16G16B16_SFLOAT: 'int' = 89
    DATA_FORMAT_R16G16B16A16_UNORM: 'int' = 90
    DATA_FORMAT_R16G16B16A16_SNORM: 'int' = 91
    DATA_FORMAT_R16G16B16A16_USCALED: 'int' = 92
    DATA_FORMAT_R16G16B16A16_SSCALED: 'int' = 93
    DATA_FORMAT_R16G16B16A16_UINT: 'int' = 94
    DATA_FORMAT_R16G16B16A16_SINT: 'int' = 95
    DATA_FORMAT_R16G16B16A16_SFLOAT: 'int' = 96
    DATA_FORMAT_R32_UINT: 'int' = 97
    DATA_FORMAT_R32_SINT: 'int' = 98
    DATA_FORMAT_R32_SFLOAT: 'int' = 99
    DATA_FORMAT_R32G32_UINT: 'int' = 100
    DATA_FORMAT_R32G32_SINT: 'int' = 101
    DATA_FORMAT_R32G32_SFLOAT: 'int' = 102
    DATA_FORMAT_R32G32B32_UINT: 'int' = 103
    DATA_FORMAT_R32G32B32_SINT: 'int' = 104
    DATA_FORMAT_R32G32B32_SFLOAT: 'int' = 105
    DATA_FORMAT_R32G32B32A32_UINT: 'int' = 106
    DATA_FORMAT_R32G32B32A32_SINT: 'int' = 107
    DATA_FORMAT_R32G32B32A32_SFLOAT: 'int' = 108
    DATA_FORMAT_R64_UINT: 'int' = 109
    DATA_FORMAT_R64_SINT: 'int' = 110
    DATA_FORMAT_R64_SFLOAT: 'int' = 111
    DATA_FORMAT_R64G64_UINT: 'int' = 112
    DATA_FORMAT_R64G64_SINT: 'int' = 113
    DATA_FORMAT_R64G64_SFLOAT: 'int' = 114
    DATA_FORMAT_R64G64B64_UINT: 'int' = 115
    DATA_FORMAT_R64G64B64_SINT: 'int' = 116
    DATA_FORMAT_R64G64B64_SFLOAT: 'int' = 117
    DATA_FORMAT_R64G64B64A64_UINT: 'int' = 118
    DATA_FORMAT_R64G64B64A64_SINT: 'int' = 119
    DATA_FORMAT_R64G64B64A64_SFLOAT: 'int' = 120
    DATA_FORMAT_B10G11R11_UFLOAT_PACK32: 'int' = 121
    DATA_FORMAT_E5B9G9R9_UFLOAT_PACK32: 'int' = 122
    DATA_FORMAT_D16_UNORM: 'int' = 123
    DATA_FORMAT_X8_D24_UNORM_PACK32: 'int' = 124
    DATA_FORMAT_D32_SFLOAT: 'int' = 125
    DATA_FORMAT_S8_UINT: 'int' = 126
    DATA_FORMAT_D16_UNORM_S8_UINT: 'int' = 127
    DATA_FORMAT_D24_UNORM_S8_UINT: 'int' = 128
    DATA_FORMAT_D32_SFLOAT_S8_UINT: 'int' = 129
    DATA_FORMAT_BC1_RGB_UNORM_BLOCK: 'int' = 130
    DATA_FORMAT_BC1_RGB_SRGB_BLOCK: 'int' = 131
    DATA_FORMAT_BC1_RGBA_UNORM_BLOCK: 'int' = 132
    DATA_FORMAT_BC1_RGBA_SRGB_BLOCK: 'int' = 133
    DATA_FORMAT_BC2_UNORM_BLOCK: 'int' = 134
    DATA_FORMAT_BC2_SRGB_BLOCK: 'int' = 135
    DATA_FORMAT_BC3_UNORM_BLOCK: 'int' = 136
    DATA_FORMAT_BC3_SRGB_BLOCK: 'int' = 137
    DATA_FORMAT_BC4_UNORM_BLOCK: 'int' = 138
    DATA_FORMAT_BC4_SNORM_BLOCK: 'int' = 139
    DATA_FORMAT_BC5_UNORM_BLOCK: 'int' = 140
    DATA_FORMAT_BC5_SNORM_BLOCK: 'int' = 141
    DATA_FORMAT_BC6H_UFLOAT_BLOCK: 'int' = 142
    DATA_FORMAT_BC6H_SFLOAT_BLOCK: 'int' = 143
    DATA_FORMAT_BC7_UNORM_BLOCK: 'int' = 144
    DATA_FORMAT_BC7_SRGB_BLOCK: 'int' = 145
    DATA_FORMAT_ETC2_R8G8B8_UNORM_BLOCK: 'int' = 146
    DATA_FORMAT_ETC2_R8G8B8_SRGB_BLOCK: 'int' = 147
    DATA_FORMAT_ETC2_R8G8B8A1_UNORM_BLOCK: 'int' = 148
    DATA_FORMAT_ETC2_R8G8B8A1_SRGB_BLOCK: 'int' = 149
    DATA_FORMAT_ETC2_R8G8B8A8_UNORM_BLOCK: 'int' = 150
    DATA_FORMAT_ETC2_R8G8B8A8_SRGB_BLOCK: 'int' = 151
    DATA_FORMAT_EAC_R11_UNORM_BLOCK: 'int' = 152
    DATA_FORMAT_EAC_R11_SNORM_BLOCK: 'int' = 153
    DATA_FORMAT_EAC_R11G11_UNORM_BLOCK: 'int' = 154
    DATA_FORMAT_EAC_R11G11_SNORM_BLOCK: 'int' = 155
    DATA_FORMAT_ASTC_4x4_UNORM_BLOCK: 'int' = 156
    DATA_FORMAT_ASTC_4x4_SRGB_BLOCK: 'int' = 157
    DATA_FORMAT_ASTC_5x4_UNORM_BLOCK: 'int' = 158
    DATA_FORMAT_ASTC_5x4_SRGB_BLOCK: 'int' = 159
    DATA_FORMAT_ASTC_5x5_UNORM_BLOCK: 'int' = 160
    DATA_FORMAT_ASTC_5x5_SRGB_BLOCK: 'int' = 161
    DATA_FORMAT_ASTC_6x5_UNORM_BLOCK: 'int' = 162
    DATA_FORMAT_ASTC_6x5_SRGB_BLOCK: 'int' = 163
    DATA_FORMAT_ASTC_6x6_UNORM_BLOCK: 'int' = 164
    DATA_FORMAT_ASTC_6x6_SRGB_BLOCK: 'int' = 165
    DATA_FORMAT_ASTC_8x5_UNORM_BLOCK: 'int' = 166
    DATA_FORMAT_ASTC_8x5_SRGB_BLOCK: 'int' = 167
    DATA_FORMAT_ASTC_8x6_UNORM_BLOCK: 'int' = 168
    DATA_FORMAT_ASTC_8x6_SRGB_BLOCK: 'int' = 169
    DATA_FORMAT_ASTC_8x8_UNORM_BLOCK: 'int' = 170
    DATA_FORMAT_ASTC_8x8_SRGB_BLOCK: 'int' = 171
    DATA_FORMAT_ASTC_10x5_UNORM_BLOCK: 'int' = 172
    DATA_FORMAT_ASTC_10x5_SRGB_BLOCK: 'int' = 173
    DATA_FORMAT_ASTC_10x6_UNORM_BLOCK: 'int' = 174
    DATA_FORMAT_ASTC_10x6_SRGB_BLOCK: 'int' = 175
    DATA_FORMAT_ASTC_10x8_UNORM_BLOCK: 'int' = 176
    DATA_FORMAT_ASTC_10x8_SRGB_BLOCK: 'int' = 177
    DATA_FORMAT_ASTC_10x10_UNORM_BLOCK: 'int' = 178
    DATA_FORMAT_ASTC_10x10_SRGB_BLOCK: 'int' = 179
    DATA_FORMAT_ASTC_12x10_UNORM_BLOCK: 'int' = 180
    DATA_FORMAT_ASTC_12x10_SRGB_BLOCK: 'int' = 181
    DATA_FORMAT_ASTC_12x12_UNORM_BLOCK: 'int' = 182
    DATA_FORMAT_ASTC_12x12_SRGB_BLOCK: 'int' = 183
    DATA_FORMAT_G8B8G8R8_422_UNORM: 'int' = 184
    DATA_FORMAT_B8G8R8G8_422_UNORM: 'int' = 185
    DATA_FORMAT_G8_B8_R8_3PLANE_420_UNORM: 'int' = 186
    DATA_FORMAT_G8_B8R8_2PLANE_420_UNORM: 'int' = 187
    DATA_FORMAT_G8_B8_R8_3PLANE_422_UNORM: 'int' = 188
    DATA_FORMAT_G8_B8R8_2PLANE_422_UNORM: 'int' = 189
    DATA_FORMAT_G8_B8_R8_3PLANE_444_UNORM: 'int' = 190
    DATA_FORMAT_R10X6_UNORM_PACK16: 'int' = 191
    DATA_FORMAT_R10X6G10X6_UNORM_2PACK16: 'int' = 192
    DATA_FORMAT_R10X6G10X6B10X6A10X6_UNORM_4PACK16: 'int' = 193
    DATA_FORMAT_G10X6B10X6G10X6R10X6_422_UNORM_4PACK16: 'int' = 194
    DATA_FORMAT_B10X6G10X6R10X6G10X6_422_UNORM_4PACK16: 'int' = 195
    DATA_FORMAT_G10X6_B10X6_R10X6_3PLANE_420_UNORM_3PACK16: 'int' = 196
    DATA_FORMAT_G10X6_B10X6R10X6_2PLANE_420_UNORM_3PACK16: 'int' = 197
    DATA_FORMAT_G10X6_B10X6_R10X6_3PLANE_422_UNORM_3PACK16: 'int' = 198
    DATA_FORMAT_G10X6_B10X6R10X6_2PLANE_422_UNORM_3PACK16: 'int' = 199
    DATA_FORMAT_G10X6_B10X6_R10X6_3PLANE_444_UNORM_3PACK16: 'int' = 200
    DATA_FORMAT_R12X4_UNORM_PACK16: 'int' = 201
    DATA_FORMAT_R12X4G12X4_UNORM_2PACK16: 'int' = 202
    DATA_FORMAT_R12X4G12X4B12X4A12X4_UNORM_4PACK16: 'int' = 203
    DATA_FORMAT_G12X4B12X4G12X4R12X4_422_UNORM_4PACK16: 'int' = 204
    DATA_FORMAT_B12X4G12X4R12X4G12X4_422_UNORM_4PACK16: 'int' = 205
    DATA_FORMAT_G12X4_B12X4_R12X4_3PLANE_420_UNORM_3PACK16: 'int' = 206
    DATA_FORMAT_G12X4_B12X4R12X4_2PLANE_420_UNORM_3PACK16: 'int' = 207
    DATA_FORMAT_G12X4_B12X4_R12X4_3PLANE_422_UNORM_3PACK16: 'int' = 208
    DATA_FORMAT_G12X4_B12X4R12X4_2PLANE_422_UNORM_3PACK16: 'int' = 209
    DATA_FORMAT_G12X4_B12X4_R12X4_3PLANE_444_UNORM_3PACK16: 'int' = 210
    DATA_FORMAT_G16B16G16R16_422_UNORM: 'int' = 211
    DATA_FORMAT_B16G16R16G16_422_UNORM: 'int' = 212
    DATA_FORMAT_G16_B16_R16_3PLANE_420_UNORM: 'int' = 213
    DATA_FORMAT_G16_B16R16_2PLANE_420_UNORM: 'int' = 214
    DATA_FORMAT_G16_B16_R16_3PLANE_422_UNORM: 'int' = 215
    DATA_FORMAT_G16_B16R16_2PLANE_422_UNORM: 'int' = 216
    DATA_FORMAT_G16_B16_R16_3PLANE_444_UNORM: 'int' = 217
    DATA_FORMAT_MAX: 'int' = 218




class RenderingDevice__BarrierMask(Enum):

    BARRIER_MASK_VERTEX: 'int' = 1
    BARRIER_MASK_FRAGMENT: 'int' = 8
    BARRIER_MASK_COMPUTE: 'int' = 2
    BARRIER_MASK_TRANSFER: 'int' = 4
    BARRIER_MASK_RASTER: 'int' = 9
    BARRIER_MASK_ALL_BARRIERS: 'int' = 32767
    BARRIER_MASK_NO_BARRIER: 'int' = 32768




class RenderingDevice__TextureType(Enum):

    TEXTURE_TYPE_1D: 'int' = 0
    TEXTURE_TYPE_2D: 'int' = 1
    TEXTURE_TYPE_3D: 'int' = 2
    TEXTURE_TYPE_CUBE: 'int' = 3
    TEXTURE_TYPE_1D_ARRAY: 'int' = 4
    TEXTURE_TYPE_2D_ARRAY: 'int' = 5
    TEXTURE_TYPE_CUBE_ARRAY: 'int' = 6
    TEXTURE_TYPE_MAX: 'int' = 7




class RenderingDevice__TextureSamples(Enum):

    TEXTURE_SAMPLES_1: 'int' = 0
    TEXTURE_SAMPLES_2: 'int' = 1
    TEXTURE_SAMPLES_4: 'int' = 2
    TEXTURE_SAMPLES_8: 'int' = 3
    TEXTURE_SAMPLES_16: 'int' = 4
    TEXTURE_SAMPLES_32: 'int' = 5
    TEXTURE_SAMPLES_64: 'int' = 6
    TEXTURE_SAMPLES_MAX: 'int' = 7




class RenderingDevice__TextureUsageBits(Enum):

    TEXTURE_USAGE_SAMPLING_BIT: 'int' = 1
    TEXTURE_USAGE_COLOR_ATTACHMENT_BIT: 'int' = 2
    TEXTURE_USAGE_DEPTH_STENCIL_ATTACHMENT_BIT: 'int' = 4
    TEXTURE_USAGE_STORAGE_BIT: 'int' = 8
    TEXTURE_USAGE_STORAGE_ATOMIC_BIT: 'int' = 16
    TEXTURE_USAGE_CPU_READ_BIT: 'int' = 32
    TEXTURE_USAGE_CAN_UPDATE_BIT: 'int' = 64
    TEXTURE_USAGE_CAN_COPY_FROM_BIT: 'int' = 128
    TEXTURE_USAGE_CAN_COPY_TO_BIT: 'int' = 256
    TEXTURE_USAGE_INPUT_ATTACHMENT_BIT: 'int' = 512




class RenderingDevice__TextureSwizzle(Enum):

    TEXTURE_SWIZZLE_IDENTITY: 'int' = 0
    TEXTURE_SWIZZLE_ZERO: 'int' = 1
    TEXTURE_SWIZZLE_ONE: 'int' = 2
    TEXTURE_SWIZZLE_R: 'int' = 3
    TEXTURE_SWIZZLE_G: 'int' = 4
    TEXTURE_SWIZZLE_B: 'int' = 5
    TEXTURE_SWIZZLE_A: 'int' = 6
    TEXTURE_SWIZZLE_MAX: 'int' = 7




class RenderingDevice__TextureSliceType(Enum):

    TEXTURE_SLICE_2D: 'int' = 0
    TEXTURE_SLICE_CUBEMAP: 'int' = 1
    TEXTURE_SLICE_3D: 'int' = 2




class RenderingDevice__SamplerFilter(Enum):

    SAMPLER_FILTER_NEAREST: 'int' = 0
    SAMPLER_FILTER_LINEAR: 'int' = 1




class RenderingDevice__SamplerRepeatMode(Enum):

    SAMPLER_REPEAT_MODE_REPEAT: 'int' = 0
    SAMPLER_REPEAT_MODE_MIRRORED_REPEAT: 'int' = 1
    SAMPLER_REPEAT_MODE_CLAMP_TO_EDGE: 'int' = 2
    SAMPLER_REPEAT_MODE_CLAMP_TO_BORDER: 'int' = 3
    SAMPLER_REPEAT_MODE_MIRROR_CLAMP_TO_EDGE: 'int' = 4
    SAMPLER_REPEAT_MODE_MAX: 'int' = 5




class RenderingDevice__SamplerBorderColor(Enum):

    SAMPLER_BORDER_COLOR_FLOAT_TRANSPARENT_BLACK: 'int' = 0
    SAMPLER_BORDER_COLOR_INT_TRANSPARENT_BLACK: 'int' = 1
    SAMPLER_BORDER_COLOR_FLOAT_OPAQUE_BLACK: 'int' = 2
    SAMPLER_BORDER_COLOR_INT_OPAQUE_BLACK: 'int' = 3
    SAMPLER_BORDER_COLOR_FLOAT_OPAQUE_WHITE: 'int' = 4
    SAMPLER_BORDER_COLOR_INT_OPAQUE_WHITE: 'int' = 5
    SAMPLER_BORDER_COLOR_MAX: 'int' = 6




class RenderingDevice__VertexFrequency(Enum):

    VERTEX_FREQUENCY_VERTEX: 'int' = 0
    VERTEX_FREQUENCY_INSTANCE: 'int' = 1




class RenderingDevice__IndexBufferFormat(Enum):

    INDEX_BUFFER_FORMAT_UINT16: 'int' = 0
    INDEX_BUFFER_FORMAT_UINT32: 'int' = 1




class RenderingDevice__StorageBufferUsage(Enum):

    STORAGE_BUFFER_USAGE_DISPATCH_INDIRECT: 'int' = 1




class RenderingDevice__BufferCreationBits(Enum):

    BUFFER_CREATION_DEVICE_ADDRESS_BIT: 'int' = 1
    BUFFER_CREATION_AS_STORAGE_BIT: 'int' = 2




class RenderingDevice__UniformType(Enum):

    UNIFORM_TYPE_SAMPLER: 'int' = 0
    UNIFORM_TYPE_SAMPLER_WITH_TEXTURE: 'int' = 1
    UNIFORM_TYPE_TEXTURE: 'int' = 2
    UNIFORM_TYPE_IMAGE: 'int' = 3
    UNIFORM_TYPE_TEXTURE_BUFFER: 'int' = 4
    UNIFORM_TYPE_SAMPLER_WITH_TEXTURE_BUFFER: 'int' = 5
    UNIFORM_TYPE_IMAGE_BUFFER: 'int' = 6
    UNIFORM_TYPE_UNIFORM_BUFFER: 'int' = 7
    UNIFORM_TYPE_STORAGE_BUFFER: 'int' = 8
    UNIFORM_TYPE_INPUT_ATTACHMENT: 'int' = 9
    UNIFORM_TYPE_MAX: 'int' = 10




class RenderingDevice__RenderPrimitive(Enum):

    RENDER_PRIMITIVE_POINTS: 'int' = 0
    RENDER_PRIMITIVE_LINES: 'int' = 1
    RENDER_PRIMITIVE_LINES_WITH_ADJACENCY: 'int' = 2
    RENDER_PRIMITIVE_LINESTRIPS: 'int' = 3
    RENDER_PRIMITIVE_LINESTRIPS_WITH_ADJACENCY: 'int' = 4
    RENDER_PRIMITIVE_TRIANGLES: 'int' = 5
    RENDER_PRIMITIVE_TRIANGLES_WITH_ADJACENCY: 'int' = 6
    RENDER_PRIMITIVE_TRIANGLE_STRIPS: 'int' = 7
    RENDER_PRIMITIVE_TRIANGLE_STRIPS_WITH_AJACENCY: 'int' = 8
    RENDER_PRIMITIVE_TRIANGLE_STRIPS_WITH_RESTART_INDEX: 'int' = 9
    RENDER_PRIMITIVE_TESSELATION_PATCH: 'int' = 10
    RENDER_PRIMITIVE_MAX: 'int' = 11




class RenderingDevice__PolygonCullMode(Enum):

    POLYGON_CULL_DISABLED: 'int' = 0
    POLYGON_CULL_FRONT: 'int' = 1
    POLYGON_CULL_BACK: 'int' = 2




class RenderingDevice__PolygonFrontFace(Enum):

    POLYGON_FRONT_FACE_CLOCKWISE: 'int' = 0
    POLYGON_FRONT_FACE_COUNTER_CLOCKWISE: 'int' = 1




class RenderingDevice__StencilOperation(Enum):

    STENCIL_OP_KEEP: 'int' = 0
    STENCIL_OP_ZERO: 'int' = 1
    STENCIL_OP_REPLACE: 'int' = 2
    STENCIL_OP_INCREMENT_AND_CLAMP: 'int' = 3
    STENCIL_OP_DECREMENT_AND_CLAMP: 'int' = 4
    STENCIL_OP_INVERT: 'int' = 5
    STENCIL_OP_INCREMENT_AND_WRAP: 'int' = 6
    STENCIL_OP_DECREMENT_AND_WRAP: 'int' = 7
    STENCIL_OP_MAX: 'int' = 8




class RenderingDevice__CompareOperator(Enum):

    COMPARE_OP_NEVER: 'int' = 0
    COMPARE_OP_LESS: 'int' = 1
    COMPARE_OP_EQUAL: 'int' = 2
    COMPARE_OP_LESS_OR_EQUAL: 'int' = 3
    COMPARE_OP_GREATER: 'int' = 4
    COMPARE_OP_NOT_EQUAL: 'int' = 5
    COMPARE_OP_GREATER_OR_EQUAL: 'int' = 6
    COMPARE_OP_ALWAYS: 'int' = 7
    COMPARE_OP_MAX: 'int' = 8




class RenderingDevice__LogicOperation(Enum):

    LOGIC_OP_CLEAR: 'int' = 0
    LOGIC_OP_AND: 'int' = 1
    LOGIC_OP_AND_REVERSE: 'int' = 2
    LOGIC_OP_COPY: 'int' = 3
    LOGIC_OP_AND_INVERTED: 'int' = 4
    LOGIC_OP_NO_OP: 'int' = 5
    LOGIC_OP_XOR: 'int' = 6
    LOGIC_OP_OR: 'int' = 7
    LOGIC_OP_NOR: 'int' = 8
    LOGIC_OP_EQUIVALENT: 'int' = 9
    LOGIC_OP_INVERT: 'int' = 10
    LOGIC_OP_OR_REVERSE: 'int' = 11
    LOGIC_OP_COPY_INVERTED: 'int' = 12
    LOGIC_OP_OR_INVERTED: 'int' = 13
    LOGIC_OP_NAND: 'int' = 14
    LOGIC_OP_SET: 'int' = 15
    LOGIC_OP_MAX: 'int' = 16




class RenderingDevice__BlendFactor(Enum):

    BLEND_FACTOR_ZERO: 'int' = 0
    BLEND_FACTOR_ONE: 'int' = 1
    BLEND_FACTOR_SRC_COLOR: 'int' = 2
    BLEND_FACTOR_ONE_MINUS_SRC_COLOR: 'int' = 3
    BLEND_FACTOR_DST_COLOR: 'int' = 4
    BLEND_FACTOR_ONE_MINUS_DST_COLOR: 'int' = 5
    BLEND_FACTOR_SRC_ALPHA: 'int' = 6
    BLEND_FACTOR_ONE_MINUS_SRC_ALPHA: 'int' = 7
    BLEND_FACTOR_DST_ALPHA: 'int' = 8
    BLEND_FACTOR_ONE_MINUS_DST_ALPHA: 'int' = 9
    BLEND_FACTOR_CONSTANT_COLOR: 'int' = 10
    BLEND_FACTOR_ONE_MINUS_CONSTANT_COLOR: 'int' = 11
    BLEND_FACTOR_CONSTANT_ALPHA: 'int' = 12
    BLEND_FACTOR_ONE_MINUS_CONSTANT_ALPHA: 'int' = 13
    BLEND_FACTOR_SRC_ALPHA_SATURATE: 'int' = 14
    BLEND_FACTOR_SRC1_COLOR: 'int' = 15
    BLEND_FACTOR_ONE_MINUS_SRC1_COLOR: 'int' = 16
    BLEND_FACTOR_SRC1_ALPHA: 'int' = 17
    BLEND_FACTOR_ONE_MINUS_SRC1_ALPHA: 'int' = 18
    BLEND_FACTOR_MAX: 'int' = 19




class RenderingDevice__BlendOperation(Enum):

    BLEND_OP_ADD: 'int' = 0
    BLEND_OP_SUBTRACT: 'int' = 1
    BLEND_OP_REVERSE_SUBTRACT: 'int' = 2
    BLEND_OP_MINIMUM: 'int' = 3
    BLEND_OP_MAXIMUM: 'int' = 4
    BLEND_OP_MAX: 'int' = 5




class RenderingDevice__PipelineDynamicStateFlags(Enum):

    DYNAMIC_STATE_LINE_WIDTH: 'int' = 1
    DYNAMIC_STATE_DEPTH_BIAS: 'int' = 2
    DYNAMIC_STATE_BLEND_CONSTANTS: 'int' = 4
    DYNAMIC_STATE_DEPTH_BOUNDS: 'int' = 8
    DYNAMIC_STATE_STENCIL_COMPARE_MASK: 'int' = 16
    DYNAMIC_STATE_STENCIL_WRITE_MASK: 'int' = 32
    DYNAMIC_STATE_STENCIL_REFERENCE: 'int' = 64




class RenderingDevice__InitialAction(Enum):

    INITIAL_ACTION_LOAD: 'int' = 0
    INITIAL_ACTION_CLEAR: 'int' = 1
    INITIAL_ACTION_DISCARD: 'int' = 2
    INITIAL_ACTION_MAX: 'int' = 3
    INITIAL_ACTION_CLEAR_REGION: 'int' = 1
    INITIAL_ACTION_CLEAR_REGION_CONTINUE: 'int' = 1
    INITIAL_ACTION_KEEP: 'int' = 0
    INITIAL_ACTION_DROP: 'int' = 2
    INITIAL_ACTION_CONTINUE: 'int' = 0




class RenderingDevice__FinalAction(Enum):

    FINAL_ACTION_STORE: 'int' = 0
    FINAL_ACTION_DISCARD: 'int' = 1
    FINAL_ACTION_MAX: 'int' = 2
    FINAL_ACTION_READ: 'int' = 0
    FINAL_ACTION_CONTINUE: 'int' = 0




class RenderingDevice__ShaderStage(Enum):

    SHADER_STAGE_VERTEX: 'int' = 0
    SHADER_STAGE_FRAGMENT: 'int' = 1
    SHADER_STAGE_TESSELATION_CONTROL: 'int' = 2
    SHADER_STAGE_TESSELATION_EVALUATION: 'int' = 3
    SHADER_STAGE_COMPUTE: 'int' = 4
    SHADER_STAGE_MAX: 'int' = 5
    SHADER_STAGE_VERTEX_BIT: 'int' = 1
    SHADER_STAGE_FRAGMENT_BIT: 'int' = 2
    SHADER_STAGE_TESSELATION_CONTROL_BIT: 'int' = 4
    SHADER_STAGE_TESSELATION_EVALUATION_BIT: 'int' = 8
    SHADER_STAGE_COMPUTE_BIT: 'int' = 16




class RenderingDevice__ShaderLanguage(Enum):

    SHADER_LANGUAGE_GLSL: 'int' = 0
    SHADER_LANGUAGE_HLSL: 'int' = 1




class RenderingDevice__PipelineSpecializationConstantType(Enum):

    PIPELINE_SPECIALIZATION_CONSTANT_TYPE_BOOL: 'int' = 0
    PIPELINE_SPECIALIZATION_CONSTANT_TYPE_INT: 'int' = 1
    PIPELINE_SPECIALIZATION_CONSTANT_TYPE_FLOAT: 'int' = 2




class RenderingDevice__Features(Enum):

    SUPPORTS_BUFFER_DEVICE_ADDRESS: 'int' = 6




class RenderingDevice__Limit(Enum):

    LIMIT_MAX_BOUND_UNIFORM_SETS: 'int' = 0
    LIMIT_MAX_FRAMEBUFFER_COLOR_ATTACHMENTS: 'int' = 1
    LIMIT_MAX_TEXTURES_PER_UNIFORM_SET: 'int' = 2
    LIMIT_MAX_SAMPLERS_PER_UNIFORM_SET: 'int' = 3
    LIMIT_MAX_STORAGE_BUFFERS_PER_UNIFORM_SET: 'int' = 4
    LIMIT_MAX_STORAGE_IMAGES_PER_UNIFORM_SET: 'int' = 5
    LIMIT_MAX_UNIFORM_BUFFERS_PER_UNIFORM_SET: 'int' = 6
    LIMIT_MAX_DRAW_INDEXED_INDEX: 'int' = 7
    LIMIT_MAX_FRAMEBUFFER_HEIGHT: 'int' = 8
    LIMIT_MAX_FRAMEBUFFER_WIDTH: 'int' = 9
    LIMIT_MAX_TEXTURE_ARRAY_LAYERS: 'int' = 10
    LIMIT_MAX_TEXTURE_SIZE_1D: 'int' = 11
    LIMIT_MAX_TEXTURE_SIZE_2D: 'int' = 12
    LIMIT_MAX_TEXTURE_SIZE_3D: 'int' = 13
    LIMIT_MAX_TEXTURE_SIZE_CUBE: 'int' = 14
    LIMIT_MAX_TEXTURES_PER_SHADER_STAGE: 'int' = 15
    LIMIT_MAX_SAMPLERS_PER_SHADER_STAGE: 'int' = 16
    LIMIT_MAX_STORAGE_BUFFERS_PER_SHADER_STAGE: 'int' = 17
    LIMIT_MAX_STORAGE_IMAGES_PER_SHADER_STAGE: 'int' = 18
    LIMIT_MAX_UNIFORM_BUFFERS_PER_SHADER_STAGE: 'int' = 19
    LIMIT_MAX_PUSH_CONSTANT_SIZE: 'int' = 20
    LIMIT_MAX_UNIFORM_BUFFER_SIZE: 'int' = 21
    LIMIT_MAX_VERTEX_INPUT_ATTRIBUTE_OFFSET: 'int' = 22
    LIMIT_MAX_VERTEX_INPUT_ATTRIBUTES: 'int' = 23
    LIMIT_MAX_VERTEX_INPUT_BINDINGS: 'int' = 24
    LIMIT_MAX_VERTEX_INPUT_BINDING_STRIDE: 'int' = 25
    LIMIT_MIN_UNIFORM_BUFFER_OFFSET_ALIGNMENT: 'int' = 26
    LIMIT_MAX_COMPUTE_SHARED_MEMORY_SIZE: 'int' = 27
    LIMIT_MAX_COMPUTE_WORKGROUP_COUNT_X: 'int' = 28
    LIMIT_MAX_COMPUTE_WORKGROUP_COUNT_Y: 'int' = 29
    LIMIT_MAX_COMPUTE_WORKGROUP_COUNT_Z: 'int' = 30
    LIMIT_MAX_COMPUTE_WORKGROUP_INVOCATIONS: 'int' = 31
    LIMIT_MAX_COMPUTE_WORKGROUP_SIZE_X: 'int' = 32
    LIMIT_MAX_COMPUTE_WORKGROUP_SIZE_Y: 'int' = 33
    LIMIT_MAX_COMPUTE_WORKGROUP_SIZE_Z: 'int' = 34
    LIMIT_MAX_VIEWPORT_DIMENSIONS_X: 'int' = 35
    LIMIT_MAX_VIEWPORT_DIMENSIONS_Y: 'int' = 36
    LIMIT_METALFX_TEMPORAL_SCALER_MIN_SCALE: 'int' = 46
    LIMIT_METALFX_TEMPORAL_SCALER_MAX_SCALE: 'int' = 47




class RenderingDevice__MemoryType(Enum):

    MEMORY_TEXTURES: 'int' = 0
    MEMORY_BUFFERS: 'int' = 1
    MEMORY_TOTAL: 'int' = 2




class RenderingDevice__BreadcrumbMarker(Enum):

    NONE: 'int' = 0
    REFLECTION_PROBES: 'int' = 65536
    SKY_PASS: 'int' = 131072
    LIGHTMAPPER_PASS: 'int' = 196608
    SHADOW_PASS_DIRECTIONAL: 'int' = 262144
    SHADOW_PASS_CUBE: 'int' = 327680
    OPAQUE_PASS: 'int' = 393216
    ALPHA_PASS: 'int' = 458752
    TRANSPARENT_PASS: 'int' = 524288
    POST_PROCESSING_PASS: 'int' = 589824
    BLIT_PASS: 'int' = 655360
    UI_PASS: 'int' = 720896
    DEBUG_PASS: 'int' = 786432




class RenderingDevice__DrawFlags(Enum):

    DRAW_DEFAULT_ALL: 'int' = 0
    DRAW_CLEAR_COLOR_0: 'int' = 1
    DRAW_CLEAR_COLOR_1: 'int' = 2
    DRAW_CLEAR_COLOR_2: 'int' = 4
    DRAW_CLEAR_COLOR_3: 'int' = 8
    DRAW_CLEAR_COLOR_4: 'int' = 16
    DRAW_CLEAR_COLOR_5: 'int' = 32
    DRAW_CLEAR_COLOR_6: 'int' = 64
    DRAW_CLEAR_COLOR_7: 'int' = 128
    DRAW_CLEAR_COLOR_MASK: 'int' = 255
    DRAW_CLEAR_COLOR_ALL: 'int' = 255
    DRAW_IGNORE_COLOR_0: 'int' = 256
    DRAW_IGNORE_COLOR_1: 'int' = 512
    DRAW_IGNORE_COLOR_2: 'int' = 1024
    DRAW_IGNORE_COLOR_3: 'int' = 2048
    DRAW_IGNORE_COLOR_4: 'int' = 4096
    DRAW_IGNORE_COLOR_5: 'int' = 8192
    DRAW_IGNORE_COLOR_6: 'int' = 16384
    DRAW_IGNORE_COLOR_7: 'int' = 32768
    DRAW_IGNORE_COLOR_MASK: 'int' = 65280
    DRAW_IGNORE_COLOR_ALL: 'int' = 65280
    DRAW_CLEAR_DEPTH: 'int' = 65536
    DRAW_IGNORE_DEPTH: 'int' = 131072
    DRAW_CLEAR_STENCIL: 'int' = 262144
    DRAW_IGNORE_STENCIL: 'int' = 524288
    DRAW_CLEAR_ALL: 'int' = 327935
    DRAW_IGNORE_ALL: 'int' = 720640




class RenderingServer__TextureType(Enum):

    TEXTURE_TYPE_2D: 'int' = 0
    TEXTURE_TYPE_LAYERED: 'int' = 1
    TEXTURE_TYPE_3D: 'int' = 2




class RenderingServer__TextureLayeredType(Enum):

    TEXTURE_LAYERED_2D_ARRAY: 'int' = 0
    TEXTURE_LAYERED_CUBEMAP: 'int' = 1
    TEXTURE_LAYERED_CUBEMAP_ARRAY: 'int' = 2




class RenderingServer__CubeMapLayer(Enum):

    CUBEMAP_LAYER_LEFT: 'int' = 0
    CUBEMAP_LAYER_RIGHT: 'int' = 1
    CUBEMAP_LAYER_BOTTOM: 'int' = 2
    CUBEMAP_LAYER_TOP: 'int' = 3
    CUBEMAP_LAYER_FRONT: 'int' = 4
    CUBEMAP_LAYER_BACK: 'int' = 5




class RenderingServer__ShaderMode(Enum):

    SHADER_SPATIAL: 'int' = 0
    SHADER_CANVAS_ITEM: 'int' = 1
    SHADER_PARTICLES: 'int' = 2
    SHADER_SKY: 'int' = 3
    SHADER_FOG: 'int' = 4
    SHADER_MAX: 'int' = 5




class RenderingServer__ArrayType(Enum):

    ARRAY_VERTEX: 'int' = 0
    ARRAY_NORMAL: 'int' = 1
    ARRAY_TANGENT: 'int' = 2
    ARRAY_COLOR: 'int' = 3
    ARRAY_TEX_UV: 'int' = 4
    ARRAY_TEX_UV2: 'int' = 5
    ARRAY_CUSTOM0: 'int' = 6
    ARRAY_CUSTOM1: 'int' = 7
    ARRAY_CUSTOM2: 'int' = 8
    ARRAY_CUSTOM3: 'int' = 9
    ARRAY_BONES: 'int' = 10
    ARRAY_WEIGHTS: 'int' = 11
    ARRAY_INDEX: 'int' = 12
    ARRAY_MAX: 'int' = 13




class RenderingServer__ArrayCustomFormat(Enum):

    ARRAY_CUSTOM_RGBA8_UNORM: 'int' = 0
    ARRAY_CUSTOM_RGBA8_SNORM: 'int' = 1
    ARRAY_CUSTOM_RG_HALF: 'int' = 2
    ARRAY_CUSTOM_RGBA_HALF: 'int' = 3
    ARRAY_CUSTOM_R_FLOAT: 'int' = 4
    ARRAY_CUSTOM_RG_FLOAT: 'int' = 5
    ARRAY_CUSTOM_RGB_FLOAT: 'int' = 6
    ARRAY_CUSTOM_RGBA_FLOAT: 'int' = 7
    ARRAY_CUSTOM_MAX: 'int' = 8




class RenderingServer__ArrayFormat(Enum):

    ARRAY_FORMAT_VERTEX: 'int' = 1
    ARRAY_FORMAT_NORMAL: 'int' = 2
    ARRAY_FORMAT_TANGENT: 'int' = 4
    ARRAY_FORMAT_COLOR: 'int' = 8
    ARRAY_FORMAT_TEX_UV: 'int' = 16
    ARRAY_FORMAT_TEX_UV2: 'int' = 32
    ARRAY_FORMAT_CUSTOM0: 'int' = 64
    ARRAY_FORMAT_CUSTOM1: 'int' = 128
    ARRAY_FORMAT_CUSTOM2: 'int' = 256
    ARRAY_FORMAT_CUSTOM3: 'int' = 512
    ARRAY_FORMAT_BONES: 'int' = 1024
    ARRAY_FORMAT_WEIGHTS: 'int' = 2048
    ARRAY_FORMAT_INDEX: 'int' = 4096
    ARRAY_FORMAT_BLEND_SHAPE_MASK: 'int' = 7
    ARRAY_FORMAT_CUSTOM_BASE: 'int' = 13
    ARRAY_FORMAT_CUSTOM_BITS: 'int' = 3
    ARRAY_FORMAT_CUSTOM0_SHIFT: 'int' = 13
    ARRAY_FORMAT_CUSTOM1_SHIFT: 'int' = 16
    ARRAY_FORMAT_CUSTOM2_SHIFT: 'int' = 19
    ARRAY_FORMAT_CUSTOM3_SHIFT: 'int' = 22
    ARRAY_FORMAT_CUSTOM_MASK: 'int' = 7
    ARRAY_COMPRESS_FLAGS_BASE: 'int' = 25
    ARRAY_FLAG_USE_2D_VERTICES: 'int' = 33554432
    ARRAY_FLAG_USE_DYNAMIC_UPDATE: 'int' = 67108864
    ARRAY_FLAG_USE_8_BONE_WEIGHTS: 'int' = 134217728
    ARRAY_FLAG_USES_EMPTY_VERTEX_ARRAY: 'int' = 268435456
    ARRAY_FLAG_COMPRESS_ATTRIBUTES: 'int' = 536870912
    ARRAY_FLAG_FORMAT_VERSION_BASE: 'int' = 35
    ARRAY_FLAG_FORMAT_VERSION_SHIFT: 'int' = 35
    ARRAY_FLAG_FORMAT_VERSION_1: 'int' = 0
    ARRAY_FLAG_FORMAT_VERSION_2: 'int' = 34359738368
    ARRAY_FLAG_FORMAT_CURRENT_VERSION: 'int' = 34359738368
    ARRAY_FLAG_FORMAT_VERSION_MASK: 'int' = 255




class RenderingServer__PrimitiveType(Enum):

    PRIMITIVE_POINTS: 'int' = 0
    PRIMITIVE_LINES: 'int' = 1
    PRIMITIVE_LINE_STRIP: 'int' = 2
    PRIMITIVE_TRIANGLES: 'int' = 3
    PRIMITIVE_TRIANGLE_STRIP: 'int' = 4
    PRIMITIVE_MAX: 'int' = 5




class RenderingServer__BlendShapeMode(Enum):

    BLEND_SHAPE_MODE_NORMALIZED: 'int' = 0
    BLEND_SHAPE_MODE_RELATIVE: 'int' = 1




class RenderingServer__MultimeshTransformFormat(Enum):

    MULTIMESH_TRANSFORM_2D: 'int' = 0
    MULTIMESH_TRANSFORM_3D: 'int' = 1




class RenderingServer__MultimeshPhysicsInterpolationQuality(Enum):

    MULTIMESH_INTERP_QUALITY_FAST: 'int' = 0
    MULTIMESH_INTERP_QUALITY_HIGH: 'int' = 1




class RenderingServer__LightProjectorFilter(Enum):

    LIGHT_PROJECTOR_FILTER_NEAREST: 'int' = 0
    LIGHT_PROJECTOR_FILTER_LINEAR: 'int' = 1
    LIGHT_PROJECTOR_FILTER_NEAREST_MIPMAPS: 'int' = 2
    LIGHT_PROJECTOR_FILTER_LINEAR_MIPMAPS: 'int' = 3
    LIGHT_PROJECTOR_FILTER_NEAREST_MIPMAPS_ANISOTROPIC: 'int' = 4
    LIGHT_PROJECTOR_FILTER_LINEAR_MIPMAPS_ANISOTROPIC: 'int' = 5




class RenderingServer__LightType(Enum):

    LIGHT_DIRECTIONAL: 'int' = 0
    LIGHT_OMNI: 'int' = 1
    LIGHT_SPOT: 'int' = 2




class RenderingServer__LightParam(Enum):

    LIGHT_PARAM_ENERGY: 'int' = 0
    LIGHT_PARAM_INDIRECT_ENERGY: 'int' = 1
    LIGHT_PARAM_VOLUMETRIC_FOG_ENERGY: 'int' = 2
    LIGHT_PARAM_SPECULAR: 'int' = 3
    LIGHT_PARAM_RANGE: 'int' = 4
    LIGHT_PARAM_SIZE: 'int' = 5
    LIGHT_PARAM_ATTENUATION: 'int' = 6
    LIGHT_PARAM_SPOT_ANGLE: 'int' = 7
    LIGHT_PARAM_SPOT_ATTENUATION: 'int' = 8
    LIGHT_PARAM_SHADOW_MAX_DISTANCE: 'int' = 9
    LIGHT_PARAM_SHADOW_SPLIT_1_OFFSET: 'int' = 10
    LIGHT_PARAM_SHADOW_SPLIT_2_OFFSET: 'int' = 11
    LIGHT_PARAM_SHADOW_SPLIT_3_OFFSET: 'int' = 12
    LIGHT_PARAM_SHADOW_FADE_START: 'int' = 13
    LIGHT_PARAM_SHADOW_NORMAL_BIAS: 'int' = 14
    LIGHT_PARAM_SHADOW_BIAS: 'int' = 15
    LIGHT_PARAM_SHADOW_PANCAKE_SIZE: 'int' = 16
    LIGHT_PARAM_SHADOW_OPACITY: 'int' = 17
    LIGHT_PARAM_SHADOW_BLUR: 'int' = 18
    LIGHT_PARAM_TRANSMITTANCE_BIAS: 'int' = 19
    LIGHT_PARAM_INTENSITY: 'int' = 20
    LIGHT_PARAM_MAX: 'int' = 21




class RenderingServer__LightBakeMode(Enum):

    LIGHT_BAKE_DISABLED: 'int' = 0
    LIGHT_BAKE_STATIC: 'int' = 1
    LIGHT_BAKE_DYNAMIC: 'int' = 2




class RenderingServer__LightOmniShadowMode(Enum):

    LIGHT_OMNI_SHADOW_DUAL_PARABOLOID: 'int' = 0
    LIGHT_OMNI_SHADOW_CUBE: 'int' = 1




class RenderingServer__LightDirectionalShadowMode(Enum):

    LIGHT_DIRECTIONAL_SHADOW_ORTHOGONAL: 'int' = 0
    LIGHT_DIRECTIONAL_SHADOW_PARALLEL_2_SPLITS: 'int' = 1
    LIGHT_DIRECTIONAL_SHADOW_PARALLEL_4_SPLITS: 'int' = 2




class RenderingServer__LightDirectionalSkyMode(Enum):

    LIGHT_DIRECTIONAL_SKY_MODE_LIGHT_AND_SKY: 'int' = 0
    LIGHT_DIRECTIONAL_SKY_MODE_LIGHT_ONLY: 'int' = 1
    LIGHT_DIRECTIONAL_SKY_MODE_SKY_ONLY: 'int' = 2




class RenderingServer__ShadowQuality(Enum):

    SHADOW_QUALITY_HARD: 'int' = 0
    SHADOW_QUALITY_SOFT_VERY_LOW: 'int' = 1
    SHADOW_QUALITY_SOFT_LOW: 'int' = 2
    SHADOW_QUALITY_SOFT_MEDIUM: 'int' = 3
    SHADOW_QUALITY_SOFT_HIGH: 'int' = 4
    SHADOW_QUALITY_SOFT_ULTRA: 'int' = 5
    SHADOW_QUALITY_MAX: 'int' = 6




class RenderingServer__ReflectionProbeUpdateMode(Enum):

    REFLECTION_PROBE_UPDATE_ONCE: 'int' = 0
    REFLECTION_PROBE_UPDATE_ALWAYS: 'int' = 1




class RenderingServer__ReflectionProbeAmbientMode(Enum):

    REFLECTION_PROBE_AMBIENT_DISABLED: 'int' = 0
    REFLECTION_PROBE_AMBIENT_ENVIRONMENT: 'int' = 1
    REFLECTION_PROBE_AMBIENT_COLOR: 'int' = 2




class RenderingServer__DecalTexture(Enum):

    DECAL_TEXTURE_ALBEDO: 'int' = 0
    DECAL_TEXTURE_NORMAL: 'int' = 1
    DECAL_TEXTURE_ORM: 'int' = 2
    DECAL_TEXTURE_EMISSION: 'int' = 3
    DECAL_TEXTURE_MAX: 'int' = 4




class RenderingServer__DecalFilter(Enum):

    DECAL_FILTER_NEAREST: 'int' = 0
    DECAL_FILTER_LINEAR: 'int' = 1
    DECAL_FILTER_NEAREST_MIPMAPS: 'int' = 2
    DECAL_FILTER_LINEAR_MIPMAPS: 'int' = 3
    DECAL_FILTER_NEAREST_MIPMAPS_ANISOTROPIC: 'int' = 4
    DECAL_FILTER_LINEAR_MIPMAPS_ANISOTROPIC: 'int' = 5




class RenderingServer__VoxelGIQuality(Enum):

    VOXEL_GI_QUALITY_LOW: 'int' = 0
    VOXEL_GI_QUALITY_HIGH: 'int' = 1




class RenderingServer__ParticlesMode(Enum):

    PARTICLES_MODE_2D: 'int' = 0
    PARTICLES_MODE_3D: 'int' = 1




class RenderingServer__ParticlesTransformAlign(Enum):

    PARTICLES_TRANSFORM_ALIGN_DISABLED: 'int' = 0
    PARTICLES_TRANSFORM_ALIGN_Z_BILLBOARD: 'int' = 1
    PARTICLES_TRANSFORM_ALIGN_Y_TO_VELOCITY: 'int' = 2
    PARTICLES_TRANSFORM_ALIGN_Z_BILLBOARD_Y_TO_VELOCITY: 'int' = 3




class RenderingServer__ParticlesDrawOrder(Enum):

    PARTICLES_DRAW_ORDER_INDEX: 'int' = 0
    PARTICLES_DRAW_ORDER_LIFETIME: 'int' = 1
    PARTICLES_DRAW_ORDER_REVERSE_LIFETIME: 'int' = 2
    PARTICLES_DRAW_ORDER_VIEW_DEPTH: 'int' = 3




class RenderingServer__ParticlesCollisionType(Enum):

    PARTICLES_COLLISION_TYPE_SPHERE_ATTRACT: 'int' = 0
    PARTICLES_COLLISION_TYPE_BOX_ATTRACT: 'int' = 1
    PARTICLES_COLLISION_TYPE_VECTOR_FIELD_ATTRACT: 'int' = 2
    PARTICLES_COLLISION_TYPE_SPHERE_COLLIDE: 'int' = 3
    PARTICLES_COLLISION_TYPE_BOX_COLLIDE: 'int' = 4
    PARTICLES_COLLISION_TYPE_SDF_COLLIDE: 'int' = 5
    PARTICLES_COLLISION_TYPE_HEIGHTFIELD_COLLIDE: 'int' = 6




class RenderingServer__ParticlesCollisionHeightfieldResolution(Enum):

    PARTICLES_COLLISION_HEIGHTFIELD_RESOLUTION_256: 'int' = 0
    PARTICLES_COLLISION_HEIGHTFIELD_RESOLUTION_512: 'int' = 1
    PARTICLES_COLLISION_HEIGHTFIELD_RESOLUTION_1024: 'int' = 2
    PARTICLES_COLLISION_HEIGHTFIELD_RESOLUTION_2048: 'int' = 3
    PARTICLES_COLLISION_HEIGHTFIELD_RESOLUTION_4096: 'int' = 4
    PARTICLES_COLLISION_HEIGHTFIELD_RESOLUTION_8192: 'int' = 5
    PARTICLES_COLLISION_HEIGHTFIELD_RESOLUTION_MAX: 'int' = 6




class RenderingServer__FogVolumeShape(Enum):

    FOG_VOLUME_SHAPE_ELLIPSOID: 'int' = 0
    FOG_VOLUME_SHAPE_CONE: 'int' = 1
    FOG_VOLUME_SHAPE_CYLINDER: 'int' = 2
    FOG_VOLUME_SHAPE_BOX: 'int' = 3
    FOG_VOLUME_SHAPE_WORLD: 'int' = 4
    FOG_VOLUME_SHAPE_MAX: 'int' = 5




class RenderingServer__ViewportScaling3DMode(Enum):

    VIEWPORT_SCALING_3D_MODE_BILINEAR: 'int' = 0
    VIEWPORT_SCALING_3D_MODE_FSR: 'int' = 1
    VIEWPORT_SCALING_3D_MODE_FSR2: 'int' = 2
    VIEWPORT_SCALING_3D_MODE_METALFX_SPATIAL: 'int' = 3
    VIEWPORT_SCALING_3D_MODE_METALFX_TEMPORAL: 'int' = 4
    VIEWPORT_SCALING_3D_MODE_MAX: 'int' = 5




class RenderingServer__ViewportUpdateMode(Enum):

    VIEWPORT_UPDATE_DISABLED: 'int' = 0
    VIEWPORT_UPDATE_ONCE: 'int' = 1
    VIEWPORT_UPDATE_WHEN_VISIBLE: 'int' = 2
    VIEWPORT_UPDATE_WHEN_PARENT_VISIBLE: 'int' = 3
    VIEWPORT_UPDATE_ALWAYS: 'int' = 4




class RenderingServer__ViewportClearMode(Enum):

    VIEWPORT_CLEAR_ALWAYS: 'int' = 0
    VIEWPORT_CLEAR_NEVER: 'int' = 1
    VIEWPORT_CLEAR_ONLY_NEXT_FRAME: 'int' = 2




class RenderingServer__ViewportEnvironmentMode(Enum):

    VIEWPORT_ENVIRONMENT_DISABLED: 'int' = 0
    VIEWPORT_ENVIRONMENT_ENABLED: 'int' = 1
    VIEWPORT_ENVIRONMENT_INHERIT: 'int' = 2
    VIEWPORT_ENVIRONMENT_MAX: 'int' = 3




class RenderingServer__ViewportSDFOversize(Enum):

    VIEWPORT_SDF_OVERSIZE_100_PERCENT: 'int' = 0
    VIEWPORT_SDF_OVERSIZE_120_PERCENT: 'int' = 1
    VIEWPORT_SDF_OVERSIZE_150_PERCENT: 'int' = 2
    VIEWPORT_SDF_OVERSIZE_200_PERCENT: 'int' = 3
    VIEWPORT_SDF_OVERSIZE_MAX: 'int' = 4




class RenderingServer__ViewportSDFScale(Enum):

    VIEWPORT_SDF_SCALE_100_PERCENT: 'int' = 0
    VIEWPORT_SDF_SCALE_50_PERCENT: 'int' = 1
    VIEWPORT_SDF_SCALE_25_PERCENT: 'int' = 2
    VIEWPORT_SDF_SCALE_MAX: 'int' = 3




class RenderingServer__ViewportMSAA(Enum):

    VIEWPORT_MSAA_DISABLED: 'int' = 0
    VIEWPORT_MSAA_2X: 'int' = 1
    VIEWPORT_MSAA_4X: 'int' = 2
    VIEWPORT_MSAA_8X: 'int' = 3
    VIEWPORT_MSAA_MAX: 'int' = 4




class RenderingServer__ViewportAnisotropicFiltering(Enum):

    VIEWPORT_ANISOTROPY_DISABLED: 'int' = 0
    VIEWPORT_ANISOTROPY_2X: 'int' = 1
    VIEWPORT_ANISOTROPY_4X: 'int' = 2
    VIEWPORT_ANISOTROPY_8X: 'int' = 3
    VIEWPORT_ANISOTROPY_16X: 'int' = 4
    VIEWPORT_ANISOTROPY_MAX: 'int' = 5




class RenderingServer__ViewportScreenSpaceAA(Enum):

    VIEWPORT_SCREEN_SPACE_AA_DISABLED: 'int' = 0
    VIEWPORT_SCREEN_SPACE_AA_FXAA: 'int' = 1
    VIEWPORT_SCREEN_SPACE_AA_MAX: 'int' = 2




class RenderingServer__ViewportOcclusionCullingBuildQuality(Enum):

    VIEWPORT_OCCLUSION_BUILD_QUALITY_LOW: 'int' = 0
    VIEWPORT_OCCLUSION_BUILD_QUALITY_MEDIUM: 'int' = 1
    VIEWPORT_OCCLUSION_BUILD_QUALITY_HIGH: 'int' = 2




class RenderingServer__ViewportRenderInfo(Enum):

    VIEWPORT_RENDER_INFO_OBJECTS_IN_FRAME: 'int' = 0
    VIEWPORT_RENDER_INFO_PRIMITIVES_IN_FRAME: 'int' = 1
    VIEWPORT_RENDER_INFO_DRAW_CALLS_IN_FRAME: 'int' = 2
    VIEWPORT_RENDER_INFO_MAX: 'int' = 3




class RenderingServer__ViewportRenderInfoType(Enum):

    VIEWPORT_RENDER_INFO_TYPE_VISIBLE: 'int' = 0
    VIEWPORT_RENDER_INFO_TYPE_SHADOW: 'int' = 1
    VIEWPORT_RENDER_INFO_TYPE_CANVAS: 'int' = 2
    VIEWPORT_RENDER_INFO_TYPE_MAX: 'int' = 3




class RenderingServer__ViewportDebugDraw(Enum):

    VIEWPORT_DEBUG_DRAW_DISABLED: 'int' = 0
    VIEWPORT_DEBUG_DRAW_UNSHADED: 'int' = 1
    VIEWPORT_DEBUG_DRAW_LIGHTING: 'int' = 2
    VIEWPORT_DEBUG_DRAW_OVERDRAW: 'int' = 3
    VIEWPORT_DEBUG_DRAW_WIREFRAME: 'int' = 4
    VIEWPORT_DEBUG_DRAW_NORMAL_BUFFER: 'int' = 5
    VIEWPORT_DEBUG_DRAW_VOXEL_GI_ALBEDO: 'int' = 6
    VIEWPORT_DEBUG_DRAW_VOXEL_GI_LIGHTING: 'int' = 7
    VIEWPORT_DEBUG_DRAW_VOXEL_GI_EMISSION: 'int' = 8
    VIEWPORT_DEBUG_DRAW_SHADOW_ATLAS: 'int' = 9
    VIEWPORT_DEBUG_DRAW_DIRECTIONAL_SHADOW_ATLAS: 'int' = 10
    VIEWPORT_DEBUG_DRAW_SCENE_LUMINANCE: 'int' = 11
    VIEWPORT_DEBUG_DRAW_SSAO: 'int' = 12
    VIEWPORT_DEBUG_DRAW_SSIL: 'int' = 13
    VIEWPORT_DEBUG_DRAW_PSSM_SPLITS: 'int' = 14
    VIEWPORT_DEBUG_DRAW_DECAL_ATLAS: 'int' = 15
    VIEWPORT_DEBUG_DRAW_SDFGI: 'int' = 16
    VIEWPORT_DEBUG_DRAW_SDFGI_PROBES: 'int' = 17
    VIEWPORT_DEBUG_DRAW_GI_BUFFER: 'int' = 18
    VIEWPORT_DEBUG_DRAW_DISABLE_LOD: 'int' = 19
    VIEWPORT_DEBUG_DRAW_CLUSTER_OMNI_LIGHTS: 'int' = 20
    VIEWPORT_DEBUG_DRAW_CLUSTER_SPOT_LIGHTS: 'int' = 21
    VIEWPORT_DEBUG_DRAW_CLUSTER_DECALS: 'int' = 22
    VIEWPORT_DEBUG_DRAW_CLUSTER_REFLECTION_PROBES: 'int' = 23
    VIEWPORT_DEBUG_DRAW_OCCLUDERS: 'int' = 24
    VIEWPORT_DEBUG_DRAW_MOTION_VECTORS: 'int' = 25
    VIEWPORT_DEBUG_DRAW_INTERNAL_BUFFER: 'int' = 26




class RenderingServer__ViewportVRSMode(Enum):

    VIEWPORT_VRS_DISABLED: 'int' = 0
    VIEWPORT_VRS_TEXTURE: 'int' = 1
    VIEWPORT_VRS_XR: 'int' = 2
    VIEWPORT_VRS_MAX: 'int' = 3




class RenderingServer__ViewportVRSUpdateMode(Enum):

    VIEWPORT_VRS_UPDATE_DISABLED: 'int' = 0
    VIEWPORT_VRS_UPDATE_ONCE: 'int' = 1
    VIEWPORT_VRS_UPDATE_ALWAYS: 'int' = 2
    VIEWPORT_VRS_UPDATE_MAX: 'int' = 3




class RenderingServer__SkyMode(Enum):

    SKY_MODE_AUTOMATIC: 'int' = 0
    SKY_MODE_QUALITY: 'int' = 1
    SKY_MODE_INCREMENTAL: 'int' = 2
    SKY_MODE_REALTIME: 'int' = 3




class RenderingServer__CompositorEffectFlags(Enum):

    COMPOSITOR_EFFECT_FLAG_ACCESS_RESOLVED_COLOR: 'int' = 1
    COMPOSITOR_EFFECT_FLAG_ACCESS_RESOLVED_DEPTH: 'int' = 2
    COMPOSITOR_EFFECT_FLAG_NEEDS_MOTION_VECTORS: 'int' = 4
    COMPOSITOR_EFFECT_FLAG_NEEDS_ROUGHNESS: 'int' = 8
    COMPOSITOR_EFFECT_FLAG_NEEDS_SEPARATE_SPECULAR: 'int' = 16




class RenderingServer__CompositorEffectCallbackType(Enum):

    COMPOSITOR_EFFECT_CALLBACK_TYPE_PRE_OPAQUE: 'int' = 0
    COMPOSITOR_EFFECT_CALLBACK_TYPE_POST_OPAQUE: 'int' = 1
    COMPOSITOR_EFFECT_CALLBACK_TYPE_POST_SKY: 'int' = 2
    COMPOSITOR_EFFECT_CALLBACK_TYPE_PRE_TRANSPARENT: 'int' = 3
    COMPOSITOR_EFFECT_CALLBACK_TYPE_POST_TRANSPARENT: 'int' = 4
    COMPOSITOR_EFFECT_CALLBACK_TYPE_ANY: 'int' = -1




class RenderingServer__EnvironmentBG(Enum):

    ENV_BG_CLEAR_COLOR: 'int' = 0
    ENV_BG_COLOR: 'int' = 1
    ENV_BG_SKY: 'int' = 2
    ENV_BG_CANVAS: 'int' = 3
    ENV_BG_KEEP: 'int' = 4
    ENV_BG_CAMERA_FEED: 'int' = 5
    ENV_BG_MAX: 'int' = 6




class RenderingServer__EnvironmentAmbientSource(Enum):

    ENV_AMBIENT_SOURCE_BG: 'int' = 0
    ENV_AMBIENT_SOURCE_DISABLED: 'int' = 1
    ENV_AMBIENT_SOURCE_COLOR: 'int' = 2
    ENV_AMBIENT_SOURCE_SKY: 'int' = 3




class RenderingServer__EnvironmentReflectionSource(Enum):

    ENV_REFLECTION_SOURCE_BG: 'int' = 0
    ENV_REFLECTION_SOURCE_DISABLED: 'int' = 1
    ENV_REFLECTION_SOURCE_SKY: 'int' = 2




class RenderingServer__EnvironmentGlowBlendMode(Enum):

    ENV_GLOW_BLEND_MODE_ADDITIVE: 'int' = 0
    ENV_GLOW_BLEND_MODE_SCREEN: 'int' = 1
    ENV_GLOW_BLEND_MODE_SOFTLIGHT: 'int' = 2
    ENV_GLOW_BLEND_MODE_REPLACE: 'int' = 3
    ENV_GLOW_BLEND_MODE_MIX: 'int' = 4




class RenderingServer__EnvironmentFogMode(Enum):

    ENV_FOG_MODE_EXPONENTIAL: 'int' = 0
    ENV_FOG_MODE_DEPTH: 'int' = 1




class RenderingServer__EnvironmentToneMapper(Enum):

    ENV_TONE_MAPPER_LINEAR: 'int' = 0
    ENV_TONE_MAPPER_REINHARD: 'int' = 1
    ENV_TONE_MAPPER_FILMIC: 'int' = 2
    ENV_TONE_MAPPER_ACES: 'int' = 3
    ENV_TONE_MAPPER_AGX: 'int' = 4




class RenderingServer__EnvironmentSSRRoughnessQuality(Enum):

    ENV_SSR_ROUGHNESS_QUALITY_DISABLED: 'int' = 0
    ENV_SSR_ROUGHNESS_QUALITY_LOW: 'int' = 1
    ENV_SSR_ROUGHNESS_QUALITY_MEDIUM: 'int' = 2
    ENV_SSR_ROUGHNESS_QUALITY_HIGH: 'int' = 3




class RenderingServer__EnvironmentSSAOQuality(Enum):

    ENV_SSAO_QUALITY_VERY_LOW: 'int' = 0
    ENV_SSAO_QUALITY_LOW: 'int' = 1
    ENV_SSAO_QUALITY_MEDIUM: 'int' = 2
    ENV_SSAO_QUALITY_HIGH: 'int' = 3
    ENV_SSAO_QUALITY_ULTRA: 'int' = 4




class RenderingServer__EnvironmentSSILQuality(Enum):

    ENV_SSIL_QUALITY_VERY_LOW: 'int' = 0
    ENV_SSIL_QUALITY_LOW: 'int' = 1
    ENV_SSIL_QUALITY_MEDIUM: 'int' = 2
    ENV_SSIL_QUALITY_HIGH: 'int' = 3
    ENV_SSIL_QUALITY_ULTRA: 'int' = 4




class RenderingServer__EnvironmentSDFGIYScale(Enum):

    ENV_SDFGI_Y_SCALE_50_PERCENT: 'int' = 0
    ENV_SDFGI_Y_SCALE_75_PERCENT: 'int' = 1
    ENV_SDFGI_Y_SCALE_100_PERCENT: 'int' = 2




class RenderingServer__EnvironmentSDFGIRayCount(Enum):

    ENV_SDFGI_RAY_COUNT_4: 'int' = 0
    ENV_SDFGI_RAY_COUNT_8: 'int' = 1
    ENV_SDFGI_RAY_COUNT_16: 'int' = 2
    ENV_SDFGI_RAY_COUNT_32: 'int' = 3
    ENV_SDFGI_RAY_COUNT_64: 'int' = 4
    ENV_SDFGI_RAY_COUNT_96: 'int' = 5
    ENV_SDFGI_RAY_COUNT_128: 'int' = 6
    ENV_SDFGI_RAY_COUNT_MAX: 'int' = 7




class RenderingServer__EnvironmentSDFGIFramesToConverge(Enum):

    ENV_SDFGI_CONVERGE_IN_5_FRAMES: 'int' = 0
    ENV_SDFGI_CONVERGE_IN_10_FRAMES: 'int' = 1
    ENV_SDFGI_CONVERGE_IN_15_FRAMES: 'int' = 2
    ENV_SDFGI_CONVERGE_IN_20_FRAMES: 'int' = 3
    ENV_SDFGI_CONVERGE_IN_25_FRAMES: 'int' = 4
    ENV_SDFGI_CONVERGE_IN_30_FRAMES: 'int' = 5
    ENV_SDFGI_CONVERGE_MAX: 'int' = 6




class RenderingServer__EnvironmentSDFGIFramesToUpdateLight(Enum):

    ENV_SDFGI_UPDATE_LIGHT_IN_1_FRAME: 'int' = 0
    ENV_SDFGI_UPDATE_LIGHT_IN_2_FRAMES: 'int' = 1
    ENV_SDFGI_UPDATE_LIGHT_IN_4_FRAMES: 'int' = 2
    ENV_SDFGI_UPDATE_LIGHT_IN_8_FRAMES: 'int' = 3
    ENV_SDFGI_UPDATE_LIGHT_IN_16_FRAMES: 'int' = 4
    ENV_SDFGI_UPDATE_LIGHT_MAX: 'int' = 5




class RenderingServer__SubSurfaceScatteringQuality(Enum):

    SUB_SURFACE_SCATTERING_QUALITY_DISABLED: 'int' = 0
    SUB_SURFACE_SCATTERING_QUALITY_LOW: 'int' = 1
    SUB_SURFACE_SCATTERING_QUALITY_MEDIUM: 'int' = 2
    SUB_SURFACE_SCATTERING_QUALITY_HIGH: 'int' = 3




class RenderingServer__DOFBokehShape(Enum):

    DOF_BOKEH_BOX: 'int' = 0
    DOF_BOKEH_HEXAGON: 'int' = 1
    DOF_BOKEH_CIRCLE: 'int' = 2




class RenderingServer__DOFBlurQuality(Enum):

    DOF_BLUR_QUALITY_VERY_LOW: 'int' = 0
    DOF_BLUR_QUALITY_LOW: 'int' = 1
    DOF_BLUR_QUALITY_MEDIUM: 'int' = 2
    DOF_BLUR_QUALITY_HIGH: 'int' = 3




class RenderingServer__InstanceType(Enum):

    INSTANCE_NONE: 'int' = 0
    INSTANCE_MESH: 'int' = 1
    INSTANCE_MULTIMESH: 'int' = 2
    INSTANCE_PARTICLES: 'int' = 3
    INSTANCE_PARTICLES_COLLISION: 'int' = 4
    INSTANCE_LIGHT: 'int' = 5
    INSTANCE_REFLECTION_PROBE: 'int' = 6
    INSTANCE_DECAL: 'int' = 7
    INSTANCE_VOXEL_GI: 'int' = 8
    INSTANCE_LIGHTMAP: 'int' = 9
    INSTANCE_OCCLUDER: 'int' = 10
    INSTANCE_VISIBLITY_NOTIFIER: 'int' = 11
    INSTANCE_FOG_VOLUME: 'int' = 12
    INSTANCE_MAX: 'int' = 13
    INSTANCE_GEOMETRY_MASK: 'int' = 14




class RenderingServer__InstanceFlags(Enum):

    INSTANCE_FLAG_USE_BAKED_LIGHT: 'int' = 0
    INSTANCE_FLAG_USE_DYNAMIC_GI: 'int' = 1
    INSTANCE_FLAG_DRAW_NEXT_FRAME_IF_VISIBLE: 'int' = 2
    INSTANCE_FLAG_IGNORE_OCCLUSION_CULLING: 'int' = 3
    INSTANCE_FLAG_MAX: 'int' = 4




class RenderingServer__ShadowCastingSetting(Enum):

    SHADOW_CASTING_SETTING_OFF: 'int' = 0
    SHADOW_CASTING_SETTING_ON: 'int' = 1
    SHADOW_CASTING_SETTING_DOUBLE_SIDED: 'int' = 2
    SHADOW_CASTING_SETTING_SHADOWS_ONLY: 'int' = 3




class RenderingServer__VisibilityRangeFadeMode(Enum):

    VISIBILITY_RANGE_FADE_DISABLED: 'int' = 0
    VISIBILITY_RANGE_FADE_SELF: 'int' = 1
    VISIBILITY_RANGE_FADE_DEPENDENCIES: 'int' = 2




class RenderingServer__BakeChannels(Enum):

    BAKE_CHANNEL_ALBEDO_ALPHA: 'int' = 0
    BAKE_CHANNEL_NORMAL: 'int' = 1
    BAKE_CHANNEL_ORM: 'int' = 2
    BAKE_CHANNEL_EMISSION: 'int' = 3




class RenderingServer__CanvasTextureChannel(Enum):

    CANVAS_TEXTURE_CHANNEL_DIFFUSE: 'int' = 0
    CANVAS_TEXTURE_CHANNEL_NORMAL: 'int' = 1
    CANVAS_TEXTURE_CHANNEL_SPECULAR: 'int' = 2




class RenderingServer__NinePatchAxisMode(Enum):

    NINE_PATCH_STRETCH: 'int' = 0
    NINE_PATCH_TILE: 'int' = 1
    NINE_PATCH_TILE_FIT: 'int' = 2




class RenderingServer__CanvasItemTextureFilter(Enum):

    CANVAS_ITEM_TEXTURE_FILTER_DEFAULT: 'int' = 0
    CANVAS_ITEM_TEXTURE_FILTER_NEAREST: 'int' = 1
    CANVAS_ITEM_TEXTURE_FILTER_LINEAR: 'int' = 2
    CANVAS_ITEM_TEXTURE_FILTER_NEAREST_WITH_MIPMAPS: 'int' = 3
    CANVAS_ITEM_TEXTURE_FILTER_LINEAR_WITH_MIPMAPS: 'int' = 4
    CANVAS_ITEM_TEXTURE_FILTER_NEAREST_WITH_MIPMAPS_ANISOTROPIC: 'int' = 5
    CANVAS_ITEM_TEXTURE_FILTER_LINEAR_WITH_MIPMAPS_ANISOTROPIC: 'int' = 6
    CANVAS_ITEM_TEXTURE_FILTER_MAX: 'int' = 7




class RenderingServer__CanvasItemTextureRepeat(Enum):

    CANVAS_ITEM_TEXTURE_REPEAT_DEFAULT: 'int' = 0
    CANVAS_ITEM_TEXTURE_REPEAT_DISABLED: 'int' = 1
    CANVAS_ITEM_TEXTURE_REPEAT_ENABLED: 'int' = 2
    CANVAS_ITEM_TEXTURE_REPEAT_MIRROR: 'int' = 3
    CANVAS_ITEM_TEXTURE_REPEAT_MAX: 'int' = 4




class RenderingServer__CanvasGroupMode(Enum):

    CANVAS_GROUP_MODE_DISABLED: 'int' = 0
    CANVAS_GROUP_MODE_CLIP_ONLY: 'int' = 1
    CANVAS_GROUP_MODE_CLIP_AND_DRAW: 'int' = 2
    CANVAS_GROUP_MODE_TRANSPARENT: 'int' = 3




class RenderingServer__CanvasLightMode(Enum):

    CANVAS_LIGHT_MODE_POINT: 'int' = 0
    CANVAS_LIGHT_MODE_DIRECTIONAL: 'int' = 1




class RenderingServer__CanvasLightBlendMode(Enum):

    CANVAS_LIGHT_BLEND_MODE_ADD: 'int' = 0
    CANVAS_LIGHT_BLEND_MODE_SUB: 'int' = 1
    CANVAS_LIGHT_BLEND_MODE_MIX: 'int' = 2




class RenderingServer__CanvasLightShadowFilter(Enum):

    CANVAS_LIGHT_FILTER_NONE: 'int' = 0
    CANVAS_LIGHT_FILTER_PCF5: 'int' = 1
    CANVAS_LIGHT_FILTER_PCF13: 'int' = 2
    CANVAS_LIGHT_FILTER_MAX: 'int' = 3




class RenderingServer__CanvasOccluderPolygonCullMode(Enum):

    CANVAS_OCCLUDER_POLYGON_CULL_DISABLED: 'int' = 0
    CANVAS_OCCLUDER_POLYGON_CULL_CLOCKWISE: 'int' = 1
    CANVAS_OCCLUDER_POLYGON_CULL_COUNTER_CLOCKWISE: 'int' = 2




class RenderingServer__GlobalShaderParameterType(Enum):

    GLOBAL_VAR_TYPE_BOOL: 'int' = 0
    GLOBAL_VAR_TYPE_BVEC2: 'int' = 1
    GLOBAL_VAR_TYPE_BVEC3: 'int' = 2
    GLOBAL_VAR_TYPE_BVEC4: 'int' = 3
    GLOBAL_VAR_TYPE_INT: 'int' = 4
    GLOBAL_VAR_TYPE_IVEC2: 'int' = 5
    GLOBAL_VAR_TYPE_IVEC3: 'int' = 6
    GLOBAL_VAR_TYPE_IVEC4: 'int' = 7
    GLOBAL_VAR_TYPE_RECT2I: 'int' = 8
    GLOBAL_VAR_TYPE_UINT: 'int' = 9
    GLOBAL_VAR_TYPE_UVEC2: 'int' = 10
    GLOBAL_VAR_TYPE_UVEC3: 'int' = 11
    GLOBAL_VAR_TYPE_UVEC4: 'int' = 12
    GLOBAL_VAR_TYPE_FLOAT: 'int' = 13
    GLOBAL_VAR_TYPE_VEC2: 'int' = 14
    GLOBAL_VAR_TYPE_VEC3: 'int' = 15
    GLOBAL_VAR_TYPE_VEC4: 'int' = 16
    GLOBAL_VAR_TYPE_COLOR: 'int' = 17
    GLOBAL_VAR_TYPE_RECT2: 'int' = 18
    GLOBAL_VAR_TYPE_MAT2: 'int' = 19
    GLOBAL_VAR_TYPE_MAT3: 'int' = 20
    GLOBAL_VAR_TYPE_MAT4: 'int' = 21
    GLOBAL_VAR_TYPE_TRANSFORM_2D: 'int' = 22
    GLOBAL_VAR_TYPE_TRANSFORM: 'int' = 23
    GLOBAL_VAR_TYPE_SAMPLER2D: 'int' = 24
    GLOBAL_VAR_TYPE_SAMPLER2DARRAY: 'int' = 25
    GLOBAL_VAR_TYPE_SAMPLER3D: 'int' = 26
    GLOBAL_VAR_TYPE_SAMPLERCUBE: 'int' = 27
    GLOBAL_VAR_TYPE_SAMPLEREXT: 'int' = 28
    GLOBAL_VAR_TYPE_MAX: 'int' = 29




class RenderingServer__RenderingInfo(Enum):

    RENDERING_INFO_TOTAL_OBJECTS_IN_FRAME: 'int' = 0
    RENDERING_INFO_TOTAL_PRIMITIVES_IN_FRAME: 'int' = 1
    RENDERING_INFO_TOTAL_DRAW_CALLS_IN_FRAME: 'int' = 2
    RENDERING_INFO_TEXTURE_MEM_USED: 'int' = 3
    RENDERING_INFO_BUFFER_MEM_USED: 'int' = 4
    RENDERING_INFO_VIDEO_MEM_USED: 'int' = 5
    RENDERING_INFO_PIPELINE_COMPILATIONS_CANVAS: 'int' = 6
    RENDERING_INFO_PIPELINE_COMPILATIONS_MESH: 'int' = 7
    RENDERING_INFO_PIPELINE_COMPILATIONS_SURFACE: 'int' = 8
    RENDERING_INFO_PIPELINE_COMPILATIONS_DRAW: 'int' = 9
    RENDERING_INFO_PIPELINE_COMPILATIONS_SPECIALIZATION: 'int' = 10




class RenderingServer__PipelineSource(Enum):

    PIPELINE_SOURCE_CANVAS: 'int' = 0
    PIPELINE_SOURCE_MESH: 'int' = 1
    PIPELINE_SOURCE_SURFACE: 'int' = 2
    PIPELINE_SOURCE_DRAW: 'int' = 3
    PIPELINE_SOURCE_SPECIALIZATION: 'int' = 4
    PIPELINE_SOURCE_MAX: 'int' = 5




class RenderingServer__Features(Enum):

    FEATURE_SHADERS: 'int' = 0
    FEATURE_MULTITHREADED: 'int' = 1




class ResourceFormatLoader__CacheMode(Enum):

    CACHE_MODE_IGNORE: 'int' = 0
    CACHE_MODE_REUSE: 'int' = 1
    CACHE_MODE_REPLACE: 'int' = 2
    CACHE_MODE_IGNORE_DEEP: 'int' = 3
    CACHE_MODE_REPLACE_DEEP: 'int' = 4




class ResourceImporter__ImportOrder(Enum):

    IMPORT_ORDER_DEFAULT: 'int' = 0
    IMPORT_ORDER_SCENE: 'int' = 100




class ResourceLoader__ThreadLoadStatus(Enum):

    THREAD_LOAD_INVALID_RESOURCE: 'int' = 0
    THREAD_LOAD_IN_PROGRESS: 'int' = 1
    THREAD_LOAD_FAILED: 'int' = 2
    THREAD_LOAD_LOADED: 'int' = 3




class ResourceLoader__CacheMode(Enum):

    CACHE_MODE_IGNORE: 'int' = 0
    CACHE_MODE_REUSE: 'int' = 1
    CACHE_MODE_REPLACE: 'int' = 2
    CACHE_MODE_IGNORE_DEEP: 'int' = 3
    CACHE_MODE_REPLACE_DEEP: 'int' = 4




class ResourceSaver__SaverFlags(Enum):

    FLAG_NONE: 'int' = 0
    FLAG_RELATIVE_PATHS: 'int' = 1
    FLAG_BUNDLE_RESOURCES: 'int' = 2
    FLAG_CHANGE_PATH: 'int' = 4
    FLAG_OMIT_EDITOR_PROPERTIES: 'int' = 8
    FLAG_SAVE_BIG_ENDIAN: 'int' = 16
    FLAG_COMPRESS: 'int' = 32
    FLAG_REPLACE_SUBRESOURCE_PATHS: 'int' = 64




class RetargetModifier3D__TransformFlag(Enum):

    TRANSFORM_FLAG_POSITION: 'int' = 1
    TRANSFORM_FLAG_ROTATION: 'int' = 2
    TRANSFORM_FLAG_SCALE: 'int' = 4
    TRANSFORM_FLAG_ALL: 'int' = 7




class RibbonTrailMesh__Shape(Enum):

    SHAPE_FLAT: 'int' = 0
    SHAPE_CROSS: 'int' = 1




class RichTextLabel__ListType(Enum):

    LIST_NUMBERS: 'int' = 0
    LIST_LETTERS: 'int' = 1
    LIST_ROMAN: 'int' = 2
    LIST_DOTS: 'int' = 3




class RichTextLabel__MenuItems(Enum):

    MENU_COPY: 'int' = 0
    MENU_SELECT_ALL: 'int' = 1
    MENU_MAX: 'int' = 2




class RichTextLabel__MetaUnderline(Enum):

    META_UNDERLINE_NEVER: 'int' = 0
    META_UNDERLINE_ALWAYS: 'int' = 1
    META_UNDERLINE_ON_HOVER: 'int' = 2




class RichTextLabel__ImageUpdateMask(Enum):

    UPDATE_TEXTURE: 'int' = 1
    UPDATE_SIZE: 'int' = 2
    UPDATE_COLOR: 'int' = 4
    UPDATE_ALIGNMENT: 'int' = 8
    UPDATE_REGION: 'int' = 16
    UPDATE_PAD: 'int' = 32
    UPDATE_TOOLTIP: 'int' = 64
    UPDATE_WIDTH_IN_PERCENT: 'int' = 128




class RigidBody2D__FreezeMode(Enum):

    FREEZE_MODE_STATIC: 'int' = 0
    FREEZE_MODE_KINEMATIC: 'int' = 1




class RigidBody2D__CenterOfMassMode(Enum):

    CENTER_OF_MASS_MODE_AUTO: 'int' = 0
    CENTER_OF_MASS_MODE_CUSTOM: 'int' = 1




class RigidBody2D__DampMode(Enum):

    DAMP_MODE_COMBINE: 'int' = 0
    DAMP_MODE_REPLACE: 'int' = 1




class RigidBody2D__CCDMode(Enum):

    CCD_MODE_DISABLED: 'int' = 0
    CCD_MODE_CAST_RAY: 'int' = 1
    CCD_MODE_CAST_SHAPE: 'int' = 2




class RigidBody3D__FreezeMode(Enum):

    FREEZE_MODE_STATIC: 'int' = 0
    FREEZE_MODE_KINEMATIC: 'int' = 1




class RigidBody3D__CenterOfMassMode(Enum):

    CENTER_OF_MASS_MODE_AUTO: 'int' = 0
    CENTER_OF_MASS_MODE_CUSTOM: 'int' = 1




class RigidBody3D__DampMode(Enum):

    DAMP_MODE_COMBINE: 'int' = 0
    DAMP_MODE_REPLACE: 'int' = 1




class SceneReplicationConfig__ReplicationMode(Enum):

    REPLICATION_MODE_NEVER: 'int' = 0
    REPLICATION_MODE_ALWAYS: 'int' = 1
    REPLICATION_MODE_ON_CHANGE: 'int' = 2




class SceneState__GenEditState(Enum):

    GEN_EDIT_STATE_DISABLED: 'int' = 0
    GEN_EDIT_STATE_INSTANCE: 'int' = 1
    GEN_EDIT_STATE_MAIN: 'int' = 2
    GEN_EDIT_STATE_MAIN_INHERITED: 'int' = 3




class SceneTree__GroupCallFlags(Enum):

    GROUP_CALL_DEFAULT: 'int' = 0
    GROUP_CALL_REVERSE: 'int' = 1
    GROUP_CALL_DEFERRED: 'int' = 2
    GROUP_CALL_UNIQUE: 'int' = 4




class ScriptLanguage__ScriptNameCasing(Enum):

    SCRIPT_NAME_CASING_AUTO: 'int' = 0
    SCRIPT_NAME_CASING_PASCAL_CASE: 'int' = 1
    SCRIPT_NAME_CASING_SNAKE_CASE: 'int' = 2
    SCRIPT_NAME_CASING_KEBAB_CASE: 'int' = 3




class ScriptLanguageExtension__LookupResultType(Enum):

    LOOKUP_RESULT_SCRIPT_LOCATION: 'int' = 0
    LOOKUP_RESULT_CLASS: 'int' = 1
    LOOKUP_RESULT_CLASS_CONSTANT: 'int' = 2
    LOOKUP_RESULT_CLASS_PROPERTY: 'int' = 3
    LOOKUP_RESULT_CLASS_METHOD: 'int' = 4
    LOOKUP_RESULT_CLASS_SIGNAL: 'int' = 5
    LOOKUP_RESULT_CLASS_ENUM: 'int' = 6
    LOOKUP_RESULT_CLASS_TBD_GLOBALSCOPE: 'int' = 7
    LOOKUP_RESULT_CLASS_ANNOTATION: 'int' = 8
    LOOKUP_RESULT_LOCAL_CONSTANT: 'int' = 9
    LOOKUP_RESULT_LOCAL_VARIABLE: 'int' = 10
    LOOKUP_RESULT_MAX: 'int' = 11




class ScriptLanguageExtension__CodeCompletionLocation(Enum):

    LOCATION_LOCAL: 'int' = 0
    LOCATION_PARENT_MASK: 'int' = 256
    LOCATION_OTHER_USER_CODE: 'int' = 512
    LOCATION_OTHER: 'int' = 1024




class ScriptLanguageExtension__CodeCompletionKind(Enum):

    CODE_COMPLETION_KIND_CLASS: 'int' = 0
    CODE_COMPLETION_KIND_FUNCTION: 'int' = 1
    CODE_COMPLETION_KIND_SIGNAL: 'int' = 2
    CODE_COMPLETION_KIND_VARIABLE: 'int' = 3
    CODE_COMPLETION_KIND_MEMBER: 'int' = 4
    CODE_COMPLETION_KIND_ENUM: 'int' = 5
    CODE_COMPLETION_KIND_CONSTANT: 'int' = 6
    CODE_COMPLETION_KIND_NODE_PATH: 'int' = 7
    CODE_COMPLETION_KIND_FILE_PATH: 'int' = 8
    CODE_COMPLETION_KIND_PLAIN_TEXT: 'int' = 9
    CODE_COMPLETION_KIND_MAX: 'int' = 10




class ScrollContainer__ScrollMode(Enum):

    SCROLL_MODE_DISABLED: 'int' = 0
    SCROLL_MODE_AUTO: 'int' = 1
    SCROLL_MODE_SHOW_ALWAYS: 'int' = 2
    SCROLL_MODE_SHOW_NEVER: 'int' = 3
    SCROLL_MODE_RESERVE: 'int' = 4




class Shader__Mode(Enum):

    MODE_SPATIAL: 'int' = 0
    MODE_CANVAS_ITEM: 'int' = 1
    MODE_PARTICLES: 'int' = 2
    MODE_SKY: 'int' = 3
    MODE_FOG: 'int' = 4




class Skeleton3D__ModifierCallbackModeProcess(Enum):

    MODIFIER_CALLBACK_MODE_PROCESS_PHYSICS: 'int' = 0
    MODIFIER_CALLBACK_MODE_PROCESS_IDLE: 'int' = 1




class SkeletonModifier3D__BoneAxis(Enum):

    BONE_AXIS_PLUS_X: 'int' = 0
    BONE_AXIS_MINUS_X: 'int' = 1
    BONE_AXIS_PLUS_Y: 'int' = 2
    BONE_AXIS_MINUS_Y: 'int' = 3
    BONE_AXIS_PLUS_Z: 'int' = 4
    BONE_AXIS_MINUS_Z: 'int' = 5




class SkeletonProfile__TailDirection(Enum):

    TAIL_DIRECTION_AVERAGE_CHILDREN: 'int' = 0
    TAIL_DIRECTION_SPECIFIC_CHILD: 'int' = 1
    TAIL_DIRECTION_END: 'int' = 2




class Sky__RadianceSize(Enum):

    RADIANCE_SIZE_32: 'int' = 0
    RADIANCE_SIZE_64: 'int' = 1
    RADIANCE_SIZE_128: 'int' = 2
    RADIANCE_SIZE_256: 'int' = 3
    RADIANCE_SIZE_512: 'int' = 4
    RADIANCE_SIZE_1024: 'int' = 5
    RADIANCE_SIZE_2048: 'int' = 6
    RADIANCE_SIZE_MAX: 'int' = 7




class Sky__ProcessMode(Enum):

    PROCESS_MODE_AUTOMATIC: 'int' = 0
    PROCESS_MODE_QUALITY: 'int' = 1
    PROCESS_MODE_INCREMENTAL: 'int' = 2
    PROCESS_MODE_REALTIME: 'int' = 3




class SliderJoint3D__Param(Enum):

    PARAM_LINEAR_LIMIT_UPPER: 'int' = 0
    PARAM_LINEAR_LIMIT_LOWER: 'int' = 1
    PARAM_LINEAR_LIMIT_SOFTNESS: 'int' = 2
    PARAM_LINEAR_LIMIT_RESTITUTION: 'int' = 3
    PARAM_LINEAR_LIMIT_DAMPING: 'int' = 4
    PARAM_LINEAR_MOTION_SOFTNESS: 'int' = 5
    PARAM_LINEAR_MOTION_RESTITUTION: 'int' = 6
    PARAM_LINEAR_MOTION_DAMPING: 'int' = 7
    PARAM_LINEAR_ORTHOGONAL_SOFTNESS: 'int' = 8
    PARAM_LINEAR_ORTHOGONAL_RESTITUTION: 'int' = 9
    PARAM_LINEAR_ORTHOGONAL_DAMPING: 'int' = 10
    PARAM_ANGULAR_LIMIT_UPPER: 'int' = 11
    PARAM_ANGULAR_LIMIT_LOWER: 'int' = 12
    PARAM_ANGULAR_LIMIT_SOFTNESS: 'int' = 13
    PARAM_ANGULAR_LIMIT_RESTITUTION: 'int' = 14
    PARAM_ANGULAR_LIMIT_DAMPING: 'int' = 15
    PARAM_ANGULAR_MOTION_SOFTNESS: 'int' = 16
    PARAM_ANGULAR_MOTION_RESTITUTION: 'int' = 17
    PARAM_ANGULAR_MOTION_DAMPING: 'int' = 18
    PARAM_ANGULAR_ORTHOGONAL_SOFTNESS: 'int' = 19
    PARAM_ANGULAR_ORTHOGONAL_RESTITUTION: 'int' = 20
    PARAM_ANGULAR_ORTHOGONAL_DAMPING: 'int' = 21
    PARAM_MAX: 'int' = 22




class SoftBody3D__DisableMode(Enum):

    DISABLE_MODE_REMOVE: 'int' = 0
    DISABLE_MODE_KEEP_ACTIVE: 'int' = 1




class SplitContainer__DraggerVisibility(Enum):

    DRAGGER_VISIBLE: 'int' = 0
    DRAGGER_HIDDEN: 'int' = 1
    DRAGGER_HIDDEN_COLLAPSED: 'int' = 2




class SpringBoneSimulator3D__BoneDirection(Enum):

    BONE_DIRECTION_PLUS_X: 'int' = 0
    BONE_DIRECTION_MINUS_X: 'int' = 1
    BONE_DIRECTION_PLUS_Y: 'int' = 2
    BONE_DIRECTION_MINUS_Y: 'int' = 3
    BONE_DIRECTION_PLUS_Z: 'int' = 4
    BONE_DIRECTION_MINUS_Z: 'int' = 5
    BONE_DIRECTION_FROM_PARENT: 'int' = 6




class SpringBoneSimulator3D__CenterFrom(Enum):

    CENTER_FROM_WORLD_ORIGIN: 'int' = 0
    CENTER_FROM_NODE: 'int' = 1
    CENTER_FROM_BONE: 'int' = 2




class SpringBoneSimulator3D__RotationAxis(Enum):

    ROTATION_AXIS_X: 'int' = 0
    ROTATION_AXIS_Y: 'int' = 1
    ROTATION_AXIS_Z: 'int' = 2
    ROTATION_AXIS_ALL: 'int' = 3




class SpriteBase3D__DrawFlags(Enum):

    FLAG_TRANSPARENT: 'int' = 0
    FLAG_SHADED: 'int' = 1
    FLAG_DOUBLE_SIDED: 'int' = 2
    FLAG_DISABLE_DEPTH_TEST: 'int' = 3
    FLAG_FIXED_SIZE: 'int' = 4
    FLAG_MAX: 'int' = 5




class SpriteBase3D__AlphaCutMode(Enum):

    ALPHA_CUT_DISABLED: 'int' = 0
    ALPHA_CUT_DISCARD: 'int' = 1
    ALPHA_CUT_OPAQUE_PREPASS: 'int' = 2
    ALPHA_CUT_HASH: 'int' = 3




class StreamPeerTCP__Status(Enum):

    STATUS_NONE: 'int' = 0
    STATUS_CONNECTING: 'int' = 1
    STATUS_CONNECTED: 'int' = 2
    STATUS_ERROR: 'int' = 3




class StreamPeerTLS__Status(Enum):

    STATUS_DISCONNECTED: 'int' = 0
    STATUS_HANDSHAKING: 'int' = 1
    STATUS_CONNECTED: 'int' = 2
    STATUS_ERROR: 'int' = 3
    STATUS_ERROR_HOSTNAME_MISMATCH: 'int' = 4




class StyleBoxTexture__AxisStretchMode(Enum):

    AXIS_STRETCH_MODE_STRETCH: 'int' = 0
    AXIS_STRETCH_MODE_TILE: 'int' = 1
    AXIS_STRETCH_MODE_TILE_FIT: 'int' = 2




class SubViewport__ClearMode(Enum):

    CLEAR_MODE_ALWAYS: 'int' = 0
    CLEAR_MODE_NEVER: 'int' = 1
    CLEAR_MODE_ONCE: 'int' = 2




class SubViewport__UpdateMode(Enum):

    UPDATE_DISABLED: 'int' = 0
    UPDATE_ONCE: 'int' = 1
    UPDATE_WHEN_VISIBLE: 'int' = 2
    UPDATE_WHEN_PARENT_VISIBLE: 'int' = 3
    UPDATE_ALWAYS: 'int' = 4




class SurfaceTool__CustomFormat(Enum):

    CUSTOM_RGBA8_UNORM: 'int' = 0
    CUSTOM_RGBA8_SNORM: 'int' = 1
    CUSTOM_RG_HALF: 'int' = 2
    CUSTOM_RGBA_HALF: 'int' = 3
    CUSTOM_R_FLOAT: 'int' = 4
    CUSTOM_RG_FLOAT: 'int' = 5
    CUSTOM_RGB_FLOAT: 'int' = 6
    CUSTOM_RGBA_FLOAT: 'int' = 7
    CUSTOM_MAX: 'int' = 8




class SurfaceTool__SkinWeightCount(Enum):

    SKIN_4_WEIGHTS: 'int' = 0
    SKIN_8_WEIGHTS: 'int' = 1




class TabBar__AlignmentMode(Enum):

    ALIGNMENT_LEFT: 'int' = 0
    ALIGNMENT_CENTER: 'int' = 1
    ALIGNMENT_RIGHT: 'int' = 2
    ALIGNMENT_MAX: 'int' = 3




class TabBar__CloseButtonDisplayPolicy(Enum):

    CLOSE_BUTTON_SHOW_NEVER: 'int' = 0
    CLOSE_BUTTON_SHOW_ACTIVE_ONLY: 'int' = 1
    CLOSE_BUTTON_SHOW_ALWAYS: 'int' = 2
    CLOSE_BUTTON_MAX: 'int' = 3




class TabContainer__TabPosition(Enum):

    POSITION_TOP: 'int' = 0
    POSITION_BOTTOM: 'int' = 1
    POSITION_MAX: 'int' = 2




class TextEdit__MenuItems(Enum):

    MENU_CUT: 'int' = 0
    MENU_COPY: 'int' = 1
    MENU_PASTE: 'int' = 2
    MENU_CLEAR: 'int' = 3
    MENU_SELECT_ALL: 'int' = 4
    MENU_UNDO: 'int' = 5
    MENU_REDO: 'int' = 6
    MENU_SUBMENU_TEXT_DIR: 'int' = 7
    MENU_DIR_INHERITED: 'int' = 8
    MENU_DIR_AUTO: 'int' = 9
    MENU_DIR_LTR: 'int' = 10
    MENU_DIR_RTL: 'int' = 11
    MENU_DISPLAY_UCC: 'int' = 12
    MENU_SUBMENU_INSERT_UCC: 'int' = 13
    MENU_INSERT_LRM: 'int' = 14
    MENU_INSERT_RLM: 'int' = 15
    MENU_INSERT_LRE: 'int' = 16
    MENU_INSERT_RLE: 'int' = 17
    MENU_INSERT_LRO: 'int' = 18
    MENU_INSERT_RLO: 'int' = 19
    MENU_INSERT_PDF: 'int' = 20
    MENU_INSERT_ALM: 'int' = 21
    MENU_INSERT_LRI: 'int' = 22
    MENU_INSERT_RLI: 'int' = 23
    MENU_INSERT_FSI: 'int' = 24
    MENU_INSERT_PDI: 'int' = 25
    MENU_INSERT_ZWJ: 'int' = 26
    MENU_INSERT_ZWNJ: 'int' = 27
    MENU_INSERT_WJ: 'int' = 28
    MENU_INSERT_SHY: 'int' = 29
    MENU_EMOJI_AND_SYMBOL: 'int' = 30
    MENU_MAX: 'int' = 31




class TextEdit__EditAction(Enum):

    ACTION_NONE: 'int' = 0
    ACTION_TYPING: 'int' = 1
    ACTION_BACKSPACE: 'int' = 2
    ACTION_DELETE: 'int' = 3




class TextEdit__SearchFlags(Enum):

    SEARCH_MATCH_CASE: 'int' = 1
    SEARCH_WHOLE_WORDS: 'int' = 2
    SEARCH_BACKWARDS: 'int' = 4




class TextEdit__CaretType(Enum):

    CARET_TYPE_LINE: 'int' = 0
    CARET_TYPE_BLOCK: 'int' = 1




class TextEdit__SelectionMode(Enum):

    SELECTION_MODE_NONE: 'int' = 0
    SELECTION_MODE_SHIFT: 'int' = 1
    SELECTION_MODE_POINTER: 'int' = 2
    SELECTION_MODE_WORD: 'int' = 3
    SELECTION_MODE_LINE: 'int' = 4




class TextEdit__LineWrappingMode(Enum):

    LINE_WRAPPING_NONE: 'int' = 0
    LINE_WRAPPING_BOUNDARY: 'int' = 1




class TextEdit__GutterType(Enum):

    GUTTER_TYPE_STRING: 'int' = 0
    GUTTER_TYPE_ICON: 'int' = 1
    GUTTER_TYPE_CUSTOM: 'int' = 2




class TextServer__FontAntialiasing(Enum):

    FONT_ANTIALIASING_NONE: 'int' = 0
    FONT_ANTIALIASING_GRAY: 'int' = 1
    FONT_ANTIALIASING_LCD: 'int' = 2




class TextServer__FontLCDSubpixelLayout(Enum):

    FONT_LCD_SUBPIXEL_LAYOUT_NONE: 'int' = 0
    FONT_LCD_SUBPIXEL_LAYOUT_HRGB: 'int' = 1
    FONT_LCD_SUBPIXEL_LAYOUT_HBGR: 'int' = 2
    FONT_LCD_SUBPIXEL_LAYOUT_VRGB: 'int' = 3
    FONT_LCD_SUBPIXEL_LAYOUT_VBGR: 'int' = 4
    FONT_LCD_SUBPIXEL_LAYOUT_MAX: 'int' = 5




class TextServer__Direction(Enum):

    DIRECTION_AUTO: 'int' = 0
    DIRECTION_LTR: 'int' = 1
    DIRECTION_RTL: 'int' = 2
    DIRECTION_INHERITED: 'int' = 3




class TextServer__Orientation(Enum):

    ORIENTATION_HORIZONTAL: 'int' = 0
    ORIENTATION_VERTICAL: 'int' = 1




class TextServer__JustificationFlag(Enum):

    JUSTIFICATION_NONE: 'int' = 0
    JUSTIFICATION_KASHIDA: 'int' = 1
    JUSTIFICATION_WORD_BOUND: 'int' = 2
    JUSTIFICATION_TRIM_EDGE_SPACES: 'int' = 4
    JUSTIFICATION_AFTER_LAST_TAB: 'int' = 8
    JUSTIFICATION_CONSTRAIN_ELLIPSIS: 'int' = 16
    JUSTIFICATION_SKIP_LAST_LINE: 'int' = 32
    JUSTIFICATION_SKIP_LAST_LINE_WITH_VISIBLE_CHARS: 'int' = 64
    JUSTIFICATION_DO_NOT_SKIP_SINGLE_LINE: 'int' = 128




class TextServer__AutowrapMode(Enum):

    AUTOWRAP_OFF: 'int' = 0
    AUTOWRAP_ARBITRARY: 'int' = 1
    AUTOWRAP_WORD: 'int' = 2
    AUTOWRAP_WORD_SMART: 'int' = 3




class TextServer__LineBreakFlag(Enum):

    BREAK_NONE: 'int' = 0
    BREAK_MANDATORY: 'int' = 1
    BREAK_WORD_BOUND: 'int' = 2
    BREAK_GRAPHEME_BOUND: 'int' = 4
    BREAK_ADAPTIVE: 'int' = 8
    BREAK_TRIM_EDGE_SPACES: 'int' = 16
    BREAK_TRIM_INDENT: 'int' = 32




class TextServer__VisibleCharactersBehavior(Enum):

    VC_CHARS_BEFORE_SHAPING: 'int' = 0
    VC_CHARS_AFTER_SHAPING: 'int' = 1
    VC_GLYPHS_AUTO: 'int' = 2
    VC_GLYPHS_LTR: 'int' = 3
    VC_GLYPHS_RTL: 'int' = 4




class TextServer__OverrunBehavior(Enum):

    OVERRUN_NO_TRIMMING: 'int' = 0
    OVERRUN_TRIM_CHAR: 'int' = 1
    OVERRUN_TRIM_WORD: 'int' = 2
    OVERRUN_TRIM_ELLIPSIS: 'int' = 3
    OVERRUN_TRIM_WORD_ELLIPSIS: 'int' = 4




class TextServer__TextOverrunFlag(Enum):

    OVERRUN_NO_TRIM: 'int' = 0
    OVERRUN_TRIM: 'int' = 1
    OVERRUN_TRIM_WORD_ONLY: 'int' = 2
    OVERRUN_ADD_ELLIPSIS: 'int' = 4
    OVERRUN_ENFORCE_ELLIPSIS: 'int' = 8
    OVERRUN_JUSTIFICATION_AWARE: 'int' = 16




class TextServer__GraphemeFlag(Enum):

    GRAPHEME_IS_VALID: 'int' = 1
    GRAPHEME_IS_RTL: 'int' = 2
    GRAPHEME_IS_VIRTUAL: 'int' = 4
    GRAPHEME_IS_SPACE: 'int' = 8
    GRAPHEME_IS_BREAK_HARD: 'int' = 16
    GRAPHEME_IS_BREAK_SOFT: 'int' = 32
    GRAPHEME_IS_TAB: 'int' = 64
    GRAPHEME_IS_ELONGATION: 'int' = 128
    GRAPHEME_IS_PUNCTUATION: 'int' = 256
    GRAPHEME_IS_UNDERSCORE: 'int' = 512
    GRAPHEME_IS_CONNECTED: 'int' = 1024
    GRAPHEME_IS_SAFE_TO_INSERT_TATWEEL: 'int' = 2048
    GRAPHEME_IS_EMBEDDED_OBJECT: 'int' = 4096
    GRAPHEME_IS_SOFT_HYPHEN: 'int' = 8192




class TextServer__Hinting(Enum):

    HINTING_NONE: 'int' = 0
    HINTING_LIGHT: 'int' = 1
    HINTING_NORMAL: 'int' = 2




class TextServer__SubpixelPositioning(Enum):

    SUBPIXEL_POSITIONING_DISABLED: 'int' = 0
    SUBPIXEL_POSITIONING_AUTO: 'int' = 1
    SUBPIXEL_POSITIONING_ONE_HALF: 'int' = 2
    SUBPIXEL_POSITIONING_ONE_QUARTER: 'int' = 3
    SUBPIXEL_POSITIONING_ONE_HALF_MAX_SIZE: 'int' = 20
    SUBPIXEL_POSITIONING_ONE_QUARTER_MAX_SIZE: 'int' = 16




class TextServer__Feature(Enum):

    FEATURE_SIMPLE_LAYOUT: 'int' = 1
    FEATURE_BIDI_LAYOUT: 'int' = 2
    FEATURE_VERTICAL_LAYOUT: 'int' = 4
    FEATURE_SHAPING: 'int' = 8
    FEATURE_KASHIDA_JUSTIFICATION: 'int' = 16
    FEATURE_BREAK_ITERATORS: 'int' = 32
    FEATURE_FONT_BITMAP: 'int' = 64
    FEATURE_FONT_DYNAMIC: 'int' = 128
    FEATURE_FONT_MSDF: 'int' = 256
    FEATURE_FONT_SYSTEM: 'int' = 512
    FEATURE_FONT_VARIABLE: 'int' = 1024
    FEATURE_CONTEXT_SENSITIVE_CASE_CONVERSION: 'int' = 2048
    FEATURE_USE_SUPPORT_DATA: 'int' = 4096
    FEATURE_UNICODE_IDENTIFIERS: 'int' = 8192
    FEATURE_UNICODE_SECURITY: 'int' = 16384




class TextServer__ContourPointTag(Enum):

    CONTOUR_CURVE_TAG_ON: 'int' = 1
    CONTOUR_CURVE_TAG_OFF_CONIC: 'int' = 0
    CONTOUR_CURVE_TAG_OFF_CUBIC: 'int' = 2




class TextServer__SpacingType(Enum):

    SPACING_GLYPH: 'int' = 0
    SPACING_SPACE: 'int' = 1
    SPACING_TOP: 'int' = 2
    SPACING_BOTTOM: 'int' = 3
    SPACING_MAX: 'int' = 4




class TextServer__FontStyle(Enum):

    FONT_BOLD: 'int' = 1
    FONT_ITALIC: 'int' = 2
    FONT_FIXED_WIDTH: 'int' = 4




class TextServer__StructuredTextParser(Enum):

    STRUCTURED_TEXT_DEFAULT: 'int' = 0
    STRUCTURED_TEXT_URI: 'int' = 1
    STRUCTURED_TEXT_FILE: 'int' = 2
    STRUCTURED_TEXT_EMAIL: 'int' = 3
    STRUCTURED_TEXT_LIST: 'int' = 4
    STRUCTURED_TEXT_GDSCRIPT: 'int' = 5
    STRUCTURED_TEXT_CUSTOM: 'int' = 6




class TextServer__FixedSizeScaleMode(Enum):

    FIXED_SIZE_SCALE_DISABLE: 'int' = 0
    FIXED_SIZE_SCALE_INTEGER_ONLY: 'int' = 1
    FIXED_SIZE_SCALE_ENABLED: 'int' = 2




class TextureButton__StretchMode(Enum):

    STRETCH_SCALE: 'int' = 0
    STRETCH_TILE: 'int' = 1
    STRETCH_KEEP: 'int' = 2
    STRETCH_KEEP_CENTERED: 'int' = 3
    STRETCH_KEEP_ASPECT: 'int' = 4
    STRETCH_KEEP_ASPECT_CENTERED: 'int' = 5
    STRETCH_KEEP_ASPECT_COVERED: 'int' = 6




class TextureLayered__LayeredType(Enum):

    LAYERED_TYPE_2D_ARRAY: 'int' = 0
    LAYERED_TYPE_CUBEMAP: 'int' = 1
    LAYERED_TYPE_CUBEMAP_ARRAY: 'int' = 2




class TextureProgressBar__FillMode(Enum):

    FILL_LEFT_TO_RIGHT: 'int' = 0
    FILL_RIGHT_TO_LEFT: 'int' = 1
    FILL_TOP_TO_BOTTOM: 'int' = 2
    FILL_BOTTOM_TO_TOP: 'int' = 3
    FILL_CLOCKWISE: 'int' = 4
    FILL_COUNTER_CLOCKWISE: 'int' = 5
    FILL_BILINEAR_LEFT_AND_RIGHT: 'int' = 6
    FILL_BILINEAR_TOP_AND_BOTTOM: 'int' = 7
    FILL_CLOCKWISE_AND_COUNTER_CLOCKWISE: 'int' = 8




class TextureRect__ExpandMode(Enum):

    EXPAND_KEEP_SIZE: 'int' = 0
    EXPAND_IGNORE_SIZE: 'int' = 1
    EXPAND_FIT_WIDTH: 'int' = 2
    EXPAND_FIT_WIDTH_PROPORTIONAL: 'int' = 3
    EXPAND_FIT_HEIGHT: 'int' = 4
    EXPAND_FIT_HEIGHT_PROPORTIONAL: 'int' = 5




class TextureRect__StretchMode(Enum):

    STRETCH_SCALE: 'int' = 0
    STRETCH_TILE: 'int' = 1
    STRETCH_KEEP: 'int' = 2
    STRETCH_KEEP_CENTERED: 'int' = 3
    STRETCH_KEEP_ASPECT: 'int' = 4
    STRETCH_KEEP_ASPECT_CENTERED: 'int' = 5
    STRETCH_KEEP_ASPECT_COVERED: 'int' = 6




class Theme__DataType(Enum):

    DATA_TYPE_COLOR: 'int' = 0
    DATA_TYPE_CONSTANT: 'int' = 1
    DATA_TYPE_FONT: 'int' = 2
    DATA_TYPE_FONT_SIZE: 'int' = 3
    DATA_TYPE_ICON: 'int' = 4
    DATA_TYPE_STYLEBOX: 'int' = 5
    DATA_TYPE_MAX: 'int' = 6




class Thread__Priority(Enum):

    PRIORITY_LOW: 'int' = 0
    PRIORITY_NORMAL: 'int' = 1
    PRIORITY_HIGH: 'int' = 2




class TileMap__VisibilityMode(Enum):

    VISIBILITY_MODE_DEFAULT: 'int' = 0
    VISIBILITY_MODE_FORCE_HIDE: 'int' = 2
    VISIBILITY_MODE_FORCE_SHOW: 'int' = 1




class TileMapLayer__DebugVisibilityMode(Enum):

    DEBUG_VISIBILITY_MODE_DEFAULT: 'int' = 0
    DEBUG_VISIBILITY_MODE_FORCE_HIDE: 'int' = 2
    DEBUG_VISIBILITY_MODE_FORCE_SHOW: 'int' = 1




class TileSet__TileShape(Enum):

    TILE_SHAPE_SQUARE: 'int' = 0
    TILE_SHAPE_ISOMETRIC: 'int' = 1
    TILE_SHAPE_HALF_OFFSET_SQUARE: 'int' = 2
    TILE_SHAPE_HEXAGON: 'int' = 3




class TileSet__TileLayout(Enum):

    TILE_LAYOUT_STACKED: 'int' = 0
    TILE_LAYOUT_STACKED_OFFSET: 'int' = 1
    TILE_LAYOUT_STAIRS_RIGHT: 'int' = 2
    TILE_LAYOUT_STAIRS_DOWN: 'int' = 3
    TILE_LAYOUT_DIAMOND_RIGHT: 'int' = 4
    TILE_LAYOUT_DIAMOND_DOWN: 'int' = 5




class TileSet__TileOffsetAxis(Enum):

    TILE_OFFSET_AXIS_HORIZONTAL: 'int' = 0
    TILE_OFFSET_AXIS_VERTICAL: 'int' = 1




class TileSet__CellNeighbor(Enum):

    CELL_NEIGHBOR_RIGHT_SIDE: 'int' = 0
    CELL_NEIGHBOR_RIGHT_CORNER: 'int' = 1
    CELL_NEIGHBOR_BOTTOM_RIGHT_SIDE: 'int' = 2
    CELL_NEIGHBOR_BOTTOM_RIGHT_CORNER: 'int' = 3
    CELL_NEIGHBOR_BOTTOM_SIDE: 'int' = 4
    CELL_NEIGHBOR_BOTTOM_CORNER: 'int' = 5
    CELL_NEIGHBOR_BOTTOM_LEFT_SIDE: 'int' = 6
    CELL_NEIGHBOR_BOTTOM_LEFT_CORNER: 'int' = 7
    CELL_NEIGHBOR_LEFT_SIDE: 'int' = 8
    CELL_NEIGHBOR_LEFT_CORNER: 'int' = 9
    CELL_NEIGHBOR_TOP_LEFT_SIDE: 'int' = 10
    CELL_NEIGHBOR_TOP_LEFT_CORNER: 'int' = 11
    CELL_NEIGHBOR_TOP_SIDE: 'int' = 12
    CELL_NEIGHBOR_TOP_CORNER: 'int' = 13
    CELL_NEIGHBOR_TOP_RIGHT_SIDE: 'int' = 14
    CELL_NEIGHBOR_TOP_RIGHT_CORNER: 'int' = 15




class TileSet__TerrainMode(Enum):

    TERRAIN_MODE_MATCH_CORNERS_AND_SIDES: 'int' = 0
    TERRAIN_MODE_MATCH_CORNERS: 'int' = 1
    TERRAIN_MODE_MATCH_SIDES: 'int' = 2




class TileSetAtlasSource__TileAnimationMode(Enum):

    TILE_ANIMATION_MODE_DEFAULT: 'int' = 0
    TILE_ANIMATION_MODE_RANDOM_START_TIMES: 'int' = 1
    TILE_ANIMATION_MODE_MAX: 'int' = 2




class Time__Month(Enum):

    MONTH_JANUARY: 'int' = 1
    MONTH_FEBRUARY: 'int' = 2
    MONTH_MARCH: 'int' = 3
    MONTH_APRIL: 'int' = 4
    MONTH_MAY: 'int' = 5
    MONTH_JUNE: 'int' = 6
    MONTH_JULY: 'int' = 7
    MONTH_AUGUST: 'int' = 8
    MONTH_SEPTEMBER: 'int' = 9
    MONTH_OCTOBER: 'int' = 10
    MONTH_NOVEMBER: 'int' = 11
    MONTH_DECEMBER: 'int' = 12




class Time__Weekday(Enum):

    WEEKDAY_SUNDAY: 'int' = 0
    WEEKDAY_MONDAY: 'int' = 1
    WEEKDAY_TUESDAY: 'int' = 2
    WEEKDAY_WEDNESDAY: 'int' = 3
    WEEKDAY_THURSDAY: 'int' = 4
    WEEKDAY_FRIDAY: 'int' = 5
    WEEKDAY_SATURDAY: 'int' = 6




class Timer__TimerProcessCallback(Enum):

    TIMER_PROCESS_PHYSICS: 'int' = 0
    TIMER_PROCESS_IDLE: 'int' = 1




class TouchScreenButton__VisibilityMode(Enum):

    VISIBILITY_ALWAYS: 'int' = 0
    VISIBILITY_TOUCHSCREEN_ONLY: 'int' = 1




class Tree__SelectMode(Enum):

    SELECT_SINGLE: 'int' = 0
    SELECT_ROW: 'int' = 1
    SELECT_MULTI: 'int' = 2




class Tree__DropModeFlags(Enum):

    DROP_MODE_DISABLED: 'int' = 0
    DROP_MODE_ON_ITEM: 'int' = 1
    DROP_MODE_INBETWEEN: 'int' = 2




class TreeItem__TreeCellMode(Enum):

    CELL_MODE_STRING: 'int' = 0
    CELL_MODE_CHECK: 'int' = 1
    CELL_MODE_RANGE: 'int' = 2
    CELL_MODE_ICON: 'int' = 3
    CELL_MODE_CUSTOM: 'int' = 4




class Tween__TweenProcessMode(Enum):

    TWEEN_PROCESS_PHYSICS: 'int' = 0
    TWEEN_PROCESS_IDLE: 'int' = 1




class Tween__TweenPauseMode(Enum):

    TWEEN_PAUSE_BOUND: 'int' = 0
    TWEEN_PAUSE_STOP: 'int' = 1
    TWEEN_PAUSE_PROCESS: 'int' = 2




class Tween__TransitionType(Enum):

    TRANS_LINEAR: 'int' = 0
    TRANS_SINE: 'int' = 1
    TRANS_QUINT: 'int' = 2
    TRANS_QUART: 'int' = 3
    TRANS_QUAD: 'int' = 4
    TRANS_EXPO: 'int' = 5
    TRANS_ELASTIC: 'int' = 6
    TRANS_CUBIC: 'int' = 7
    TRANS_CIRC: 'int' = 8
    TRANS_BOUNCE: 'int' = 9
    TRANS_BACK: 'int' = 10
    TRANS_SPRING: 'int' = 11




class Tween__EaseType(Enum):

    EASE_IN: 'int' = 0
    EASE_OUT: 'int' = 1
    EASE_IN_OUT: 'int' = 2
    EASE_OUT_IN: 'int' = 3




class UPNP__UPNPResult(Enum):

    UPNP_RESULT_SUCCESS: 'int' = 0
    UPNP_RESULT_NOT_AUTHORIZED: 'int' = 1
    UPNP_RESULT_PORT_MAPPING_NOT_FOUND: 'int' = 2
    UPNP_RESULT_INCONSISTENT_PARAMETERS: 'int' = 3
    UPNP_RESULT_NO_SUCH_ENTRY_IN_ARRAY: 'int' = 4
    UPNP_RESULT_ACTION_FAILED: 'int' = 5
    UPNP_RESULT_SRC_IP_WILDCARD_NOT_PERMITTED: 'int' = 6
    UPNP_RESULT_EXT_PORT_WILDCARD_NOT_PERMITTED: 'int' = 7
    UPNP_RESULT_INT_PORT_WILDCARD_NOT_PERMITTED: 'int' = 8
    UPNP_RESULT_REMOTE_HOST_MUST_BE_WILDCARD: 'int' = 9
    UPNP_RESULT_EXT_PORT_MUST_BE_WILDCARD: 'int' = 10
    UPNP_RESULT_NO_PORT_MAPS_AVAILABLE: 'int' = 11
    UPNP_RESULT_CONFLICT_WITH_OTHER_MECHANISM: 'int' = 12
    UPNP_RESULT_CONFLICT_WITH_OTHER_MAPPING: 'int' = 13
    UPNP_RESULT_SAME_PORT_VALUES_REQUIRED: 'int' = 14
    UPNP_RESULT_ONLY_PERMANENT_LEASE_SUPPORTED: 'int' = 15
    UPNP_RESULT_INVALID_GATEWAY: 'int' = 16
    UPNP_RESULT_INVALID_PORT: 'int' = 17
    UPNP_RESULT_INVALID_PROTOCOL: 'int' = 18
    UPNP_RESULT_INVALID_DURATION: 'int' = 19
    UPNP_RESULT_INVALID_ARGS: 'int' = 20
    UPNP_RESULT_INVALID_RESPONSE: 'int' = 21
    UPNP_RESULT_INVALID_PARAM: 'int' = 22
    UPNP_RESULT_HTTP_ERROR: 'int' = 23
    UPNP_RESULT_SOCKET_ERROR: 'int' = 24
    UPNP_RESULT_MEM_ALLOC_ERROR: 'int' = 25
    UPNP_RESULT_NO_GATEWAY: 'int' = 26
    UPNP_RESULT_NO_DEVICES: 'int' = 27
    UPNP_RESULT_UNKNOWN_ERROR: 'int' = 28




class UPNPDevice__IGDStatus(Enum):

    IGD_STATUS_OK: 'int' = 0
    IGD_STATUS_HTTP_ERROR: 'int' = 1
    IGD_STATUS_HTTP_EMPTY: 'int' = 2
    IGD_STATUS_NO_URLS: 'int' = 3
    IGD_STATUS_NO_IGD: 'int' = 4
    IGD_STATUS_DISCONNECTED: 'int' = 5
    IGD_STATUS_UNKNOWN_DEVICE: 'int' = 6
    IGD_STATUS_INVALID_CONTROL: 'int' = 7
    IGD_STATUS_MALLOC_ERROR: 'int' = 8
    IGD_STATUS_UNKNOWN_ERROR: 'int' = 9




class UndoRedo__MergeMode(Enum):

    MERGE_DISABLE: 'int' = 0
    MERGE_ENDS: 'int' = 1
    MERGE_ALL: 'int' = 2




class Viewport__PositionalShadowAtlasQuadrantSubdiv(Enum):

    SHADOW_ATLAS_QUADRANT_SUBDIV_DISABLED: 'int' = 0
    SHADOW_ATLAS_QUADRANT_SUBDIV_1: 'int' = 1
    SHADOW_ATLAS_QUADRANT_SUBDIV_4: 'int' = 2
    SHADOW_ATLAS_QUADRANT_SUBDIV_16: 'int' = 3
    SHADOW_ATLAS_QUADRANT_SUBDIV_64: 'int' = 4
    SHADOW_ATLAS_QUADRANT_SUBDIV_256: 'int' = 5
    SHADOW_ATLAS_QUADRANT_SUBDIV_1024: 'int' = 6
    SHADOW_ATLAS_QUADRANT_SUBDIV_MAX: 'int' = 7




class Viewport__Scaling3DMode(Enum):

    SCALING_3D_MODE_BILINEAR: 'int' = 0
    SCALING_3D_MODE_FSR: 'int' = 1
    SCALING_3D_MODE_FSR2: 'int' = 2
    SCALING_3D_MODE_METALFX_SPATIAL: 'int' = 3
    SCALING_3D_MODE_METALFX_TEMPORAL: 'int' = 4
    SCALING_3D_MODE_MAX: 'int' = 5




class Viewport__MSAA(Enum):

    MSAA_DISABLED: 'int' = 0
    MSAA_2X: 'int' = 1
    MSAA_4X: 'int' = 2
    MSAA_8X: 'int' = 3
    MSAA_MAX: 'int' = 4




class Viewport__AnisotropicFiltering(Enum):

    ANISOTROPY_DISABLED: 'int' = 0
    ANISOTROPY_2X: 'int' = 1
    ANISOTROPY_4X: 'int' = 2
    ANISOTROPY_8X: 'int' = 3
    ANISOTROPY_16X: 'int' = 4
    ANISOTROPY_MAX: 'int' = 5




class Viewport__ScreenSpaceAA(Enum):

    SCREEN_SPACE_AA_DISABLED: 'int' = 0
    SCREEN_SPACE_AA_FXAA: 'int' = 1
    SCREEN_SPACE_AA_MAX: 'int' = 2




class Viewport__RenderInfo(Enum):

    RENDER_INFO_OBJECTS_IN_FRAME: 'int' = 0
    RENDER_INFO_PRIMITIVES_IN_FRAME: 'int' = 1
    RENDER_INFO_DRAW_CALLS_IN_FRAME: 'int' = 2
    RENDER_INFO_MAX: 'int' = 3




class Viewport__RenderInfoType(Enum):

    RENDER_INFO_TYPE_VISIBLE: 'int' = 0
    RENDER_INFO_TYPE_SHADOW: 'int' = 1
    RENDER_INFO_TYPE_CANVAS: 'int' = 2
    RENDER_INFO_TYPE_MAX: 'int' = 3




class Viewport__DebugDraw(Enum):

    DEBUG_DRAW_DISABLED: 'int' = 0
    DEBUG_DRAW_UNSHADED: 'int' = 1
    DEBUG_DRAW_LIGHTING: 'int' = 2
    DEBUG_DRAW_OVERDRAW: 'int' = 3
    DEBUG_DRAW_WIREFRAME: 'int' = 4
    DEBUG_DRAW_NORMAL_BUFFER: 'int' = 5
    DEBUG_DRAW_VOXEL_GI_ALBEDO: 'int' = 6
    DEBUG_DRAW_VOXEL_GI_LIGHTING: 'int' = 7
    DEBUG_DRAW_VOXEL_GI_EMISSION: 'int' = 8
    DEBUG_DRAW_SHADOW_ATLAS: 'int' = 9
    DEBUG_DRAW_DIRECTIONAL_SHADOW_ATLAS: 'int' = 10
    DEBUG_DRAW_SCENE_LUMINANCE: 'int' = 11
    DEBUG_DRAW_SSAO: 'int' = 12
    DEBUG_DRAW_SSIL: 'int' = 13
    DEBUG_DRAW_PSSM_SPLITS: 'int' = 14
    DEBUG_DRAW_DECAL_ATLAS: 'int' = 15
    DEBUG_DRAW_SDFGI: 'int' = 16
    DEBUG_DRAW_SDFGI_PROBES: 'int' = 17
    DEBUG_DRAW_GI_BUFFER: 'int' = 18
    DEBUG_DRAW_DISABLE_LOD: 'int' = 19
    DEBUG_DRAW_CLUSTER_OMNI_LIGHTS: 'int' = 20
    DEBUG_DRAW_CLUSTER_SPOT_LIGHTS: 'int' = 21
    DEBUG_DRAW_CLUSTER_DECALS: 'int' = 22
    DEBUG_DRAW_CLUSTER_REFLECTION_PROBES: 'int' = 23
    DEBUG_DRAW_OCCLUDERS: 'int' = 24
    DEBUG_DRAW_MOTION_VECTORS: 'int' = 25
    DEBUG_DRAW_INTERNAL_BUFFER: 'int' = 26




class Viewport__DefaultCanvasItemTextureFilter(Enum):

    DEFAULT_CANVAS_ITEM_TEXTURE_FILTER_NEAREST: 'int' = 0
    DEFAULT_CANVAS_ITEM_TEXTURE_FILTER_LINEAR: 'int' = 1
    DEFAULT_CANVAS_ITEM_TEXTURE_FILTER_LINEAR_WITH_MIPMAPS: 'int' = 2
    DEFAULT_CANVAS_ITEM_TEXTURE_FILTER_NEAREST_WITH_MIPMAPS: 'int' = 3
    DEFAULT_CANVAS_ITEM_TEXTURE_FILTER_MAX: 'int' = 4




class Viewport__DefaultCanvasItemTextureRepeat(Enum):

    DEFAULT_CANVAS_ITEM_TEXTURE_REPEAT_DISABLED: 'int' = 0
    DEFAULT_CANVAS_ITEM_TEXTURE_REPEAT_ENABLED: 'int' = 1
    DEFAULT_CANVAS_ITEM_TEXTURE_REPEAT_MIRROR: 'int' = 2
    DEFAULT_CANVAS_ITEM_TEXTURE_REPEAT_MAX: 'int' = 3




class Viewport__SDFOversize(Enum):

    SDF_OVERSIZE_100_PERCENT: 'int' = 0
    SDF_OVERSIZE_120_PERCENT: 'int' = 1
    SDF_OVERSIZE_150_PERCENT: 'int' = 2
    SDF_OVERSIZE_200_PERCENT: 'int' = 3
    SDF_OVERSIZE_MAX: 'int' = 4




class Viewport__SDFScale(Enum):

    SDF_SCALE_100_PERCENT: 'int' = 0
    SDF_SCALE_50_PERCENT: 'int' = 1
    SDF_SCALE_25_PERCENT: 'int' = 2
    SDF_SCALE_MAX: 'int' = 3




class Viewport__VRSMode(Enum):

    VRS_DISABLED: 'int' = 0
    VRS_TEXTURE: 'int' = 1
    VRS_XR: 'int' = 2
    VRS_MAX: 'int' = 3




class Viewport__VRSUpdateMode(Enum):

    VRS_UPDATE_DISABLED: 'int' = 0
    VRS_UPDATE_ONCE: 'int' = 1
    VRS_UPDATE_ALWAYS: 'int' = 2
    VRS_UPDATE_MAX: 'int' = 3




class VisibleOnScreenEnabler2D__EnableMode(Enum):

    ENABLE_MODE_INHERIT: 'int' = 0
    ENABLE_MODE_ALWAYS: 'int' = 1
    ENABLE_MODE_WHEN_PAUSED: 'int' = 2




class VisibleOnScreenEnabler3D__EnableMode(Enum):

    ENABLE_MODE_INHERIT: 'int' = 0
    ENABLE_MODE_ALWAYS: 'int' = 1
    ENABLE_MODE_WHEN_PAUSED: 'int' = 2




class VisualShader__Type(Enum):

    TYPE_VERTEX: 'int' = 0
    TYPE_FRAGMENT: 'int' = 1
    TYPE_LIGHT: 'int' = 2
    TYPE_START: 'int' = 3
    TYPE_PROCESS: 'int' = 4
    TYPE_COLLIDE: 'int' = 5
    TYPE_START_CUSTOM: 'int' = 6
    TYPE_PROCESS_CUSTOM: 'int' = 7
    TYPE_SKY: 'int' = 8
    TYPE_FOG: 'int' = 9
    TYPE_MAX: 'int' = 10




class VisualShader__VaryingMode(Enum):

    VARYING_MODE_VERTEX_TO_FRAG_LIGHT: 'int' = 0
    VARYING_MODE_FRAG_TO_LIGHT: 'int' = 1
    VARYING_MODE_MAX: 'int' = 2




class VisualShader__VaryingType(Enum):

    VARYING_TYPE_FLOAT: 'int' = 0
    VARYING_TYPE_INT: 'int' = 1
    VARYING_TYPE_UINT: 'int' = 2
    VARYING_TYPE_VECTOR_2D: 'int' = 3
    VARYING_TYPE_VECTOR_3D: 'int' = 4
    VARYING_TYPE_VECTOR_4D: 'int' = 5
    VARYING_TYPE_BOOLEAN: 'int' = 6
    VARYING_TYPE_TRANSFORM: 'int' = 7
    VARYING_TYPE_MAX: 'int' = 8




class VisualShaderNode__PortType(Enum):

    PORT_TYPE_SCALAR: 'int' = 0
    PORT_TYPE_SCALAR_INT: 'int' = 1
    PORT_TYPE_SCALAR_UINT: 'int' = 2
    PORT_TYPE_VECTOR_2D: 'int' = 3
    PORT_TYPE_VECTOR_3D: 'int' = 4
    PORT_TYPE_VECTOR_4D: 'int' = 5
    PORT_TYPE_BOOLEAN: 'int' = 6
    PORT_TYPE_TRANSFORM: 'int' = 7
    PORT_TYPE_SAMPLER: 'int' = 8
    PORT_TYPE_MAX: 'int' = 9




class VisualShaderNodeBillboard__BillboardType(Enum):

    BILLBOARD_TYPE_DISABLED: 'int' = 0
    BILLBOARD_TYPE_ENABLED: 'int' = 1
    BILLBOARD_TYPE_FIXED_Y: 'int' = 2
    BILLBOARD_TYPE_PARTICLES: 'int' = 3
    BILLBOARD_TYPE_MAX: 'int' = 4




class VisualShaderNodeClamp__OpType(Enum):

    OP_TYPE_FLOAT: 'int' = 0
    OP_TYPE_INT: 'int' = 1
    OP_TYPE_UINT: 'int' = 2
    OP_TYPE_VECTOR_2D: 'int' = 3
    OP_TYPE_VECTOR_3D: 'int' = 4
    OP_TYPE_VECTOR_4D: 'int' = 5
    OP_TYPE_MAX: 'int' = 6




class VisualShaderNodeColorFunc__Function(Enum):

    FUNC_GRAYSCALE: 'int' = 0
    FUNC_HSV2RGB: 'int' = 1
    FUNC_RGB2HSV: 'int' = 2
    FUNC_SEPIA: 'int' = 3
    FUNC_LINEAR_TO_SRGB: 'int' = 4
    FUNC_SRGB_TO_LINEAR: 'int' = 5
    FUNC_MAX: 'int' = 6




class VisualShaderNodeColorOp__Operator(Enum):

    OP_SCREEN: 'int' = 0
    OP_DIFFERENCE: 'int' = 1
    OP_DARKEN: 'int' = 2
    OP_LIGHTEN: 'int' = 3
    OP_OVERLAY: 'int' = 4
    OP_DODGE: 'int' = 5
    OP_BURN: 'int' = 6
    OP_SOFT_LIGHT: 'int' = 7
    OP_HARD_LIGHT: 'int' = 8
    OP_MAX: 'int' = 9




class VisualShaderNodeCompare__ComparisonType(Enum):

    CTYPE_SCALAR: 'int' = 0
    CTYPE_SCALAR_INT: 'int' = 1
    CTYPE_SCALAR_UINT: 'int' = 2
    CTYPE_VECTOR_2D: 'int' = 3
    CTYPE_VECTOR_3D: 'int' = 4
    CTYPE_VECTOR_4D: 'int' = 5
    CTYPE_BOOLEAN: 'int' = 6
    CTYPE_TRANSFORM: 'int' = 7
    CTYPE_MAX: 'int' = 8




class VisualShaderNodeCompare__Function(Enum):

    FUNC_EQUAL: 'int' = 0
    FUNC_NOT_EQUAL: 'int' = 1
    FUNC_GREATER_THAN: 'int' = 2
    FUNC_GREATER_THAN_EQUAL: 'int' = 3
    FUNC_LESS_THAN: 'int' = 4
    FUNC_LESS_THAN_EQUAL: 'int' = 5
    FUNC_MAX: 'int' = 6




class VisualShaderNodeCompare__Condition(Enum):

    COND_ALL: 'int' = 0
    COND_ANY: 'int' = 1
    COND_MAX: 'int' = 2




class VisualShaderNodeCubemap__Source(Enum):

    SOURCE_TEXTURE: 'int' = 0
    SOURCE_PORT: 'int' = 1
    SOURCE_MAX: 'int' = 2




class VisualShaderNodeCubemap__TextureType(Enum):

    TYPE_DATA: 'int' = 0
    TYPE_COLOR: 'int' = 1
    TYPE_NORMAL_MAP: 'int' = 2
    TYPE_MAX: 'int' = 3




class VisualShaderNodeDerivativeFunc__OpType(Enum):

    OP_TYPE_SCALAR: 'int' = 0
    OP_TYPE_VECTOR_2D: 'int' = 1
    OP_TYPE_VECTOR_3D: 'int' = 2
    OP_TYPE_VECTOR_4D: 'int' = 3
    OP_TYPE_MAX: 'int' = 4




class VisualShaderNodeDerivativeFunc__Function(Enum):

    FUNC_SUM: 'int' = 0
    FUNC_X: 'int' = 1
    FUNC_Y: 'int' = 2
    FUNC_MAX: 'int' = 3




class VisualShaderNodeDerivativeFunc__Precision(Enum):

    PRECISION_NONE: 'int' = 0
    PRECISION_COARSE: 'int' = 1
    PRECISION_FINE: 'int' = 2
    PRECISION_MAX: 'int' = 3




class VisualShaderNodeFloatFunc__Function(Enum):

    FUNC_SIN: 'int' = 0
    FUNC_COS: 'int' = 1
    FUNC_TAN: 'int' = 2
    FUNC_ASIN: 'int' = 3
    FUNC_ACOS: 'int' = 4
    FUNC_ATAN: 'int' = 5
    FUNC_SINH: 'int' = 6
    FUNC_COSH: 'int' = 7
    FUNC_TANH: 'int' = 8
    FUNC_LOG: 'int' = 9
    FUNC_EXP: 'int' = 10
    FUNC_SQRT: 'int' = 11
    FUNC_ABS: 'int' = 12
    FUNC_SIGN: 'int' = 13
    FUNC_FLOOR: 'int' = 14
    FUNC_ROUND: 'int' = 15
    FUNC_CEIL: 'int' = 16
    FUNC_FRACT: 'int' = 17
    FUNC_SATURATE: 'int' = 18
    FUNC_NEGATE: 'int' = 19
    FUNC_ACOSH: 'int' = 20
    FUNC_ASINH: 'int' = 21
    FUNC_ATANH: 'int' = 22
    FUNC_DEGREES: 'int' = 23
    FUNC_EXP2: 'int' = 24
    FUNC_INVERSE_SQRT: 'int' = 25
    FUNC_LOG2: 'int' = 26
    FUNC_RADIANS: 'int' = 27
    FUNC_RECIPROCAL: 'int' = 28
    FUNC_ROUNDEVEN: 'int' = 29
    FUNC_TRUNC: 'int' = 30
    FUNC_ONEMINUS: 'int' = 31
    FUNC_MAX: 'int' = 32




class VisualShaderNodeFloatOp__Operator(Enum):

    OP_ADD: 'int' = 0
    OP_SUB: 'int' = 1
    OP_MUL: 'int' = 2
    OP_DIV: 'int' = 3
    OP_MOD: 'int' = 4
    OP_POW: 'int' = 5
    OP_MAX: 'int' = 6
    OP_MIN: 'int' = 7
    OP_ATAN2: 'int' = 8
    OP_STEP: 'int' = 9
    OP_ENUM_SIZE: 'int' = 10




class VisualShaderNodeFloatParameter__Hint(Enum):

    HINT_NONE: 'int' = 0
    HINT_RANGE: 'int' = 1
    HINT_RANGE_STEP: 'int' = 2
    HINT_MAX: 'int' = 3




class VisualShaderNodeIntFunc__Function(Enum):

    FUNC_ABS: 'int' = 0
    FUNC_NEGATE: 'int' = 1
    FUNC_SIGN: 'int' = 2
    FUNC_BITWISE_NOT: 'int' = 3
    FUNC_MAX: 'int' = 4




class VisualShaderNodeIntOp__Operator(Enum):

    OP_ADD: 'int' = 0
    OP_SUB: 'int' = 1
    OP_MUL: 'int' = 2
    OP_DIV: 'int' = 3
    OP_MOD: 'int' = 4
    OP_MAX: 'int' = 5
    OP_MIN: 'int' = 6
    OP_BITWISE_AND: 'int' = 7
    OP_BITWISE_OR: 'int' = 8
    OP_BITWISE_XOR: 'int' = 9
    OP_BITWISE_LEFT_SHIFT: 'int' = 10
    OP_BITWISE_RIGHT_SHIFT: 'int' = 11
    OP_ENUM_SIZE: 'int' = 12




class VisualShaderNodeIntParameter__Hint(Enum):

    HINT_NONE: 'int' = 0
    HINT_RANGE: 'int' = 1
    HINT_RANGE_STEP: 'int' = 2
    HINT_ENUM: 'int' = 3
    HINT_MAX: 'int' = 4




class VisualShaderNodeIs__Function(Enum):

    FUNC_IS_INF: 'int' = 0
    FUNC_IS_NAN: 'int' = 1
    FUNC_MAX: 'int' = 2




class VisualShaderNodeMix__OpType(Enum):

    OP_TYPE_SCALAR: 'int' = 0
    OP_TYPE_VECTOR_2D: 'int' = 1
    OP_TYPE_VECTOR_2D_SCALAR: 'int' = 2
    OP_TYPE_VECTOR_3D: 'int' = 3
    OP_TYPE_VECTOR_3D_SCALAR: 'int' = 4
    OP_TYPE_VECTOR_4D: 'int' = 5
    OP_TYPE_VECTOR_4D_SCALAR: 'int' = 6
    OP_TYPE_MAX: 'int' = 7




class VisualShaderNodeMultiplyAdd__OpType(Enum):

    OP_TYPE_SCALAR: 'int' = 0
    OP_TYPE_VECTOR_2D: 'int' = 1
    OP_TYPE_VECTOR_3D: 'int' = 2
    OP_TYPE_VECTOR_4D: 'int' = 3
    OP_TYPE_MAX: 'int' = 4




class VisualShaderNodeParameter__Qualifier(Enum):

    QUAL_NONE: 'int' = 0
    QUAL_GLOBAL: 'int' = 1
    QUAL_INSTANCE: 'int' = 2
    QUAL_MAX: 'int' = 3




class VisualShaderNodeParticleAccelerator__Mode(Enum):

    MODE_LINEAR: 'int' = 0
    MODE_RADIAL: 'int' = 1
    MODE_TANGENTIAL: 'int' = 2
    MODE_MAX: 'int' = 3




class VisualShaderNodeParticleEmit__EmitFlags(Enum):

    EMIT_FLAG_POSITION: 'int' = 1
    EMIT_FLAG_ROT_SCALE: 'int' = 2
    EMIT_FLAG_VELOCITY: 'int' = 4
    EMIT_FLAG_COLOR: 'int' = 8
    EMIT_FLAG_CUSTOM: 'int' = 16




class VisualShaderNodeParticleRandomness__OpType(Enum):

    OP_TYPE_SCALAR: 'int' = 0
    OP_TYPE_VECTOR_2D: 'int' = 1
    OP_TYPE_VECTOR_3D: 'int' = 2
    OP_TYPE_VECTOR_4D: 'int' = 3
    OP_TYPE_MAX: 'int' = 4




class VisualShaderNodeRemap__OpType(Enum):

    OP_TYPE_SCALAR: 'int' = 0
    OP_TYPE_VECTOR_2D: 'int' = 1
    OP_TYPE_VECTOR_2D_SCALAR: 'int' = 2
    OP_TYPE_VECTOR_3D: 'int' = 3
    OP_TYPE_VECTOR_3D_SCALAR: 'int' = 4
    OP_TYPE_VECTOR_4D: 'int' = 5
    OP_TYPE_VECTOR_4D_SCALAR: 'int' = 6
    OP_TYPE_MAX: 'int' = 7




class VisualShaderNodeSample3D__Source(Enum):

    SOURCE_TEXTURE: 'int' = 0
    SOURCE_PORT: 'int' = 1
    SOURCE_MAX: 'int' = 2




class VisualShaderNodeSmoothStep__OpType(Enum):

    OP_TYPE_SCALAR: 'int' = 0
    OP_TYPE_VECTOR_2D: 'int' = 1
    OP_TYPE_VECTOR_2D_SCALAR: 'int' = 2
    OP_TYPE_VECTOR_3D: 'int' = 3
    OP_TYPE_VECTOR_3D_SCALAR: 'int' = 4
    OP_TYPE_VECTOR_4D: 'int' = 5
    OP_TYPE_VECTOR_4D_SCALAR: 'int' = 6
    OP_TYPE_MAX: 'int' = 7




class VisualShaderNodeStep__OpType(Enum):

    OP_TYPE_SCALAR: 'int' = 0
    OP_TYPE_VECTOR_2D: 'int' = 1
    OP_TYPE_VECTOR_2D_SCALAR: 'int' = 2
    OP_TYPE_VECTOR_3D: 'int' = 3
    OP_TYPE_VECTOR_3D_SCALAR: 'int' = 4
    OP_TYPE_VECTOR_4D: 'int' = 5
    OP_TYPE_VECTOR_4D_SCALAR: 'int' = 6
    OP_TYPE_MAX: 'int' = 7




class VisualShaderNodeSwitch__OpType(Enum):

    OP_TYPE_FLOAT: 'int' = 0
    OP_TYPE_INT: 'int' = 1
    OP_TYPE_UINT: 'int' = 2
    OP_TYPE_VECTOR_2D: 'int' = 3
    OP_TYPE_VECTOR_3D: 'int' = 4
    OP_TYPE_VECTOR_4D: 'int' = 5
    OP_TYPE_BOOLEAN: 'int' = 6
    OP_TYPE_TRANSFORM: 'int' = 7
    OP_TYPE_MAX: 'int' = 8




class VisualShaderNodeTexture__Source(Enum):

    SOURCE_TEXTURE: 'int' = 0
    SOURCE_SCREEN: 'int' = 1
    SOURCE_2D_TEXTURE: 'int' = 2
    SOURCE_2D_NORMAL: 'int' = 3
    SOURCE_DEPTH: 'int' = 4
    SOURCE_PORT: 'int' = 5
    SOURCE_3D_NORMAL: 'int' = 6
    SOURCE_ROUGHNESS: 'int' = 7
    SOURCE_MAX: 'int' = 8




class VisualShaderNodeTexture__TextureType(Enum):

    TYPE_DATA: 'int' = 0
    TYPE_COLOR: 'int' = 1
    TYPE_NORMAL_MAP: 'int' = 2
    TYPE_MAX: 'int' = 3




class VisualShaderNodeTextureParameter__TextureType(Enum):

    TYPE_DATA: 'int' = 0
    TYPE_COLOR: 'int' = 1
    TYPE_NORMAL_MAP: 'int' = 2
    TYPE_ANISOTROPY: 'int' = 3
    TYPE_MAX: 'int' = 4




class VisualShaderNodeTextureParameter__ColorDefault(Enum):

    COLOR_DEFAULT_WHITE: 'int' = 0
    COLOR_DEFAULT_BLACK: 'int' = 1
    COLOR_DEFAULT_TRANSPARENT: 'int' = 2
    COLOR_DEFAULT_MAX: 'int' = 3




class VisualShaderNodeTextureParameter__TextureFilter(Enum):

    FILTER_DEFAULT: 'int' = 0
    FILTER_NEAREST: 'int' = 1
    FILTER_LINEAR: 'int' = 2
    FILTER_NEAREST_MIPMAP: 'int' = 3
    FILTER_LINEAR_MIPMAP: 'int' = 4
    FILTER_NEAREST_MIPMAP_ANISOTROPIC: 'int' = 5
    FILTER_LINEAR_MIPMAP_ANISOTROPIC: 'int' = 6
    FILTER_MAX: 'int' = 7




class VisualShaderNodeTextureParameter__TextureRepeat(Enum):

    REPEAT_DEFAULT: 'int' = 0
    REPEAT_ENABLED: 'int' = 1
    REPEAT_DISABLED: 'int' = 2
    REPEAT_MAX: 'int' = 3




class VisualShaderNodeTextureParameter__TextureSource(Enum):

    SOURCE_NONE: 'int' = 0
    SOURCE_SCREEN: 'int' = 1
    SOURCE_DEPTH: 'int' = 2
    SOURCE_NORMAL_ROUGHNESS: 'int' = 3
    SOURCE_MAX: 'int' = 4




class VisualShaderNodeTransformFunc__Function(Enum):

    FUNC_INVERSE: 'int' = 0
    FUNC_TRANSPOSE: 'int' = 1
    FUNC_MAX: 'int' = 2




class VisualShaderNodeTransformOp__Operator(Enum):

    OP_AxB: 'int' = 0
    OP_BxA: 'int' = 1
    OP_AxB_COMP: 'int' = 2
    OP_BxA_COMP: 'int' = 3
    OP_ADD: 'int' = 4
    OP_A_MINUS_B: 'int' = 5
    OP_B_MINUS_A: 'int' = 6
    OP_A_DIV_B: 'int' = 7
    OP_B_DIV_A: 'int' = 8
    OP_MAX: 'int' = 9




class VisualShaderNodeTransformVecMult__Operator(Enum):

    OP_AxB: 'int' = 0
    OP_BxA: 'int' = 1
    OP_3x3_AxB: 'int' = 2
    OP_3x3_BxA: 'int' = 3
    OP_MAX: 'int' = 4




class VisualShaderNodeUIntFunc__Function(Enum):

    FUNC_NEGATE: 'int' = 0
    FUNC_BITWISE_NOT: 'int' = 1
    FUNC_MAX: 'int' = 2




class VisualShaderNodeUIntOp__Operator(Enum):

    OP_ADD: 'int' = 0
    OP_SUB: 'int' = 1
    OP_MUL: 'int' = 2
    OP_DIV: 'int' = 3
    OP_MOD: 'int' = 4
    OP_MAX: 'int' = 5
    OP_MIN: 'int' = 6
    OP_BITWISE_AND: 'int' = 7
    OP_BITWISE_OR: 'int' = 8
    OP_BITWISE_XOR: 'int' = 9
    OP_BITWISE_LEFT_SHIFT: 'int' = 10
    OP_BITWISE_RIGHT_SHIFT: 'int' = 11
    OP_ENUM_SIZE: 'int' = 12




class VisualShaderNodeUVFunc__Function(Enum):

    FUNC_PANNING: 'int' = 0
    FUNC_SCALING: 'int' = 1
    FUNC_MAX: 'int' = 2




class VisualShaderNodeVectorBase__OpType(Enum):

    OP_TYPE_VECTOR_2D: 'int' = 0
    OP_TYPE_VECTOR_3D: 'int' = 1
    OP_TYPE_VECTOR_4D: 'int' = 2
    OP_TYPE_MAX: 'int' = 3




class VisualShaderNodeVectorFunc__Function(Enum):

    FUNC_NORMALIZE: 'int' = 0
    FUNC_SATURATE: 'int' = 1
    FUNC_NEGATE: 'int' = 2
    FUNC_RECIPROCAL: 'int' = 3
    FUNC_ABS: 'int' = 4
    FUNC_ACOS: 'int' = 5
    FUNC_ACOSH: 'int' = 6
    FUNC_ASIN: 'int' = 7
    FUNC_ASINH: 'int' = 8
    FUNC_ATAN: 'int' = 9
    FUNC_ATANH: 'int' = 10
    FUNC_CEIL: 'int' = 11
    FUNC_COS: 'int' = 12
    FUNC_COSH: 'int' = 13
    FUNC_DEGREES: 'int' = 14
    FUNC_EXP: 'int' = 15
    FUNC_EXP2: 'int' = 16
    FUNC_FLOOR: 'int' = 17
    FUNC_FRACT: 'int' = 18
    FUNC_INVERSE_SQRT: 'int' = 19
    FUNC_LOG: 'int' = 20
    FUNC_LOG2: 'int' = 21
    FUNC_RADIANS: 'int' = 22
    FUNC_ROUND: 'int' = 23
    FUNC_ROUNDEVEN: 'int' = 24
    FUNC_SIGN: 'int' = 25
    FUNC_SIN: 'int' = 26
    FUNC_SINH: 'int' = 27
    FUNC_SQRT: 'int' = 28
    FUNC_TAN: 'int' = 29
    FUNC_TANH: 'int' = 30
    FUNC_TRUNC: 'int' = 31
    FUNC_ONEMINUS: 'int' = 32
    FUNC_MAX: 'int' = 33




class VisualShaderNodeVectorOp__Operator(Enum):

    OP_ADD: 'int' = 0
    OP_SUB: 'int' = 1
    OP_MUL: 'int' = 2
    OP_DIV: 'int' = 3
    OP_MOD: 'int' = 4
    OP_POW: 'int' = 5
    OP_MAX: 'int' = 6
    OP_MIN: 'int' = 7
    OP_CROSS: 'int' = 8
    OP_ATAN2: 'int' = 9
    OP_REFLECT: 'int' = 10
    OP_STEP: 'int' = 11
    OP_ENUM_SIZE: 'int' = 12




class VoxelGI__Subdiv(Enum):

    SUBDIV_64: 'int' = 0
    SUBDIV_128: 'int' = 1
    SUBDIV_256: 'int' = 2
    SUBDIV_512: 'int' = 3
    SUBDIV_MAX: 'int' = 4




class WebRTCDataChannel__WriteMode(Enum):

    WRITE_MODE_TEXT: 'int' = 0
    WRITE_MODE_BINARY: 'int' = 1




class WebRTCDataChannel__ChannelState(Enum):

    STATE_CONNECTING: 'int' = 0
    STATE_OPEN: 'int' = 1
    STATE_CLOSING: 'int' = 2
    STATE_CLOSED: 'int' = 3




class WebRTCPeerConnection__ConnectionState(Enum):

    STATE_NEW: 'int' = 0
    STATE_CONNECTING: 'int' = 1
    STATE_CONNECTED: 'int' = 2
    STATE_DISCONNECTED: 'int' = 3
    STATE_FAILED: 'int' = 4
    STATE_CLOSED: 'int' = 5




class WebRTCPeerConnection__GatheringState(Enum):

    GATHERING_STATE_NEW: 'int' = 0
    GATHERING_STATE_GATHERING: 'int' = 1
    GATHERING_STATE_COMPLETE: 'int' = 2




class WebRTCPeerConnection__SignalingState(Enum):

    SIGNALING_STATE_STABLE: 'int' = 0
    SIGNALING_STATE_HAVE_LOCAL_OFFER: 'int' = 1
    SIGNALING_STATE_HAVE_REMOTE_OFFER: 'int' = 2
    SIGNALING_STATE_HAVE_LOCAL_PRANSWER: 'int' = 3
    SIGNALING_STATE_HAVE_REMOTE_PRANSWER: 'int' = 4
    SIGNALING_STATE_CLOSED: 'int' = 5




class WebSocketPeer__WriteMode(Enum):

    WRITE_MODE_TEXT: 'int' = 0
    WRITE_MODE_BINARY: 'int' = 1




class WebSocketPeer__State(Enum):

    STATE_CONNECTING: 'int' = 0
    STATE_OPEN: 'int' = 1
    STATE_CLOSING: 'int' = 2
    STATE_CLOSED: 'int' = 3




class WebXRInterface__TargetRayMode(Enum):

    TARGET_RAY_MODE_UNKNOWN: 'int' = 0
    TARGET_RAY_MODE_GAZE: 'int' = 1
    TARGET_RAY_MODE_TRACKED_POINTER: 'int' = 2
    TARGET_RAY_MODE_SCREEN: 'int' = 3




class Window__Mode(Enum):

    MODE_WINDOWED: 'int' = 0
    MODE_MINIMIZED: 'int' = 1
    MODE_MAXIMIZED: 'int' = 2
    MODE_FULLSCREEN: 'int' = 3
    MODE_EXCLUSIVE_FULLSCREEN: 'int' = 4




class Window__Flags(Enum):

    FLAG_RESIZE_DISABLED: 'int' = 0
    FLAG_BORDERLESS: 'int' = 1
    FLAG_ALWAYS_ON_TOP: 'int' = 2
    FLAG_TRANSPARENT: 'int' = 3
    FLAG_NO_FOCUS: 'int' = 4
    FLAG_POPUP: 'int' = 5
    FLAG_EXTEND_TO_TITLE: 'int' = 6
    FLAG_MOUSE_PASSTHROUGH: 'int' = 7
    FLAG_SHARP_CORNERS: 'int' = 8
    FLAG_EXCLUDE_FROM_CAPTURE: 'int' = 9
    FLAG_MAX: 'int' = 10




class Window__ContentScaleMode(Enum):

    CONTENT_SCALE_MODE_DISABLED: 'int' = 0
    CONTENT_SCALE_MODE_CANVAS_ITEMS: 'int' = 1
    CONTENT_SCALE_MODE_VIEWPORT: 'int' = 2




class Window__ContentScaleAspect(Enum):

    CONTENT_SCALE_ASPECT_IGNORE: 'int' = 0
    CONTENT_SCALE_ASPECT_KEEP: 'int' = 1
    CONTENT_SCALE_ASPECT_KEEP_WIDTH: 'int' = 2
    CONTENT_SCALE_ASPECT_KEEP_HEIGHT: 'int' = 3
    CONTENT_SCALE_ASPECT_EXPAND: 'int' = 4




class Window__ContentScaleStretch(Enum):

    CONTENT_SCALE_STRETCH_FRACTIONAL: 'int' = 0
    CONTENT_SCALE_STRETCH_INTEGER: 'int' = 1




class Window__LayoutDirection(Enum):

    LAYOUT_DIRECTION_INHERITED: 'int' = 0
    LAYOUT_DIRECTION_APPLICATION_LOCALE: 'int' = 1
    LAYOUT_DIRECTION_LTR: 'int' = 2
    LAYOUT_DIRECTION_RTL: 'int' = 3
    LAYOUT_DIRECTION_SYSTEM_LOCALE: 'int' = 4
    LAYOUT_DIRECTION_MAX: 'int' = 5
    LAYOUT_DIRECTION_LOCALE: 'int' = 1




class Window__WindowInitialPosition(Enum):

    WINDOW_INITIAL_POSITION_ABSOLUTE: 'int' = 0
    WINDOW_INITIAL_POSITION_CENTER_PRIMARY_SCREEN: 'int' = 1
    WINDOW_INITIAL_POSITION_CENTER_MAIN_WINDOW_SCREEN: 'int' = 2
    WINDOW_INITIAL_POSITION_CENTER_OTHER_SCREEN: 'int' = 3
    WINDOW_INITIAL_POSITION_CENTER_SCREEN_WITH_MOUSE_FOCUS: 'int' = 4
    WINDOW_INITIAL_POSITION_CENTER_SCREEN_WITH_KEYBOARD_FOCUS: 'int' = 5




class XMLParser__NodeType(Enum):

    NODE_NONE: 'int' = 0
    NODE_ELEMENT: 'int' = 1
    NODE_ELEMENT_END: 'int' = 2
    NODE_TEXT: 'int' = 3
    NODE_COMMENT: 'int' = 4
    NODE_CDATA: 'int' = 5
    NODE_UNKNOWN: 'int' = 6




class XRBodyModifier3D__BodyUpdate(Enum):

    BODY_UPDATE_UPPER_BODY: 'int' = 1
    BODY_UPDATE_LOWER_BODY: 'int' = 2
    BODY_UPDATE_HANDS: 'int' = 4




class XRBodyModifier3D__BoneUpdate(Enum):

    BONE_UPDATE_FULL: 'int' = 0
    BONE_UPDATE_ROTATION_ONLY: 'int' = 1
    BONE_UPDATE_MAX: 'int' = 2




class XRBodyTracker__BodyFlags(Enum):

    BODY_FLAG_UPPER_BODY_SUPPORTED: 'int' = 1
    BODY_FLAG_LOWER_BODY_SUPPORTED: 'int' = 2
    BODY_FLAG_HANDS_SUPPORTED: 'int' = 4




class XRBodyTracker__Joint(Enum):

    JOINT_ROOT: 'int' = 0
    JOINT_HIPS: 'int' = 1
    JOINT_SPINE: 'int' = 2
    JOINT_CHEST: 'int' = 3
    JOINT_UPPER_CHEST: 'int' = 4
    JOINT_NECK: 'int' = 5
    JOINT_HEAD: 'int' = 6
    JOINT_HEAD_TIP: 'int' = 7
    JOINT_LEFT_SHOULDER: 'int' = 8
    JOINT_LEFT_UPPER_ARM: 'int' = 9
    JOINT_LEFT_LOWER_ARM: 'int' = 10
    JOINT_RIGHT_SHOULDER: 'int' = 11
    JOINT_RIGHT_UPPER_ARM: 'int' = 12
    JOINT_RIGHT_LOWER_ARM: 'int' = 13
    JOINT_LEFT_UPPER_LEG: 'int' = 14
    JOINT_LEFT_LOWER_LEG: 'int' = 15
    JOINT_LEFT_FOOT: 'int' = 16
    JOINT_LEFT_TOES: 'int' = 17
    JOINT_RIGHT_UPPER_LEG: 'int' = 18
    JOINT_RIGHT_LOWER_LEG: 'int' = 19
    JOINT_RIGHT_FOOT: 'int' = 20
    JOINT_RIGHT_TOES: 'int' = 21
    JOINT_LEFT_HAND: 'int' = 22
    JOINT_LEFT_PALM: 'int' = 23
    JOINT_LEFT_WRIST: 'int' = 24
    JOINT_LEFT_THUMB_METACARPAL: 'int' = 25
    JOINT_LEFT_THUMB_PHALANX_PROXIMAL: 'int' = 26
    JOINT_LEFT_THUMB_PHALANX_DISTAL: 'int' = 27
    JOINT_LEFT_THUMB_TIP: 'int' = 28
    JOINT_LEFT_INDEX_FINGER_METACARPAL: 'int' = 29
    JOINT_LEFT_INDEX_FINGER_PHALANX_PROXIMAL: 'int' = 30
    JOINT_LEFT_INDEX_FINGER_PHALANX_INTERMEDIATE: 'int' = 31
    JOINT_LEFT_INDEX_FINGER_PHALANX_DISTAL: 'int' = 32
    JOINT_LEFT_INDEX_FINGER_TIP: 'int' = 33
    JOINT_LEFT_MIDDLE_FINGER_METACARPAL: 'int' = 34
    JOINT_LEFT_MIDDLE_FINGER_PHALANX_PROXIMAL: 'int' = 35
    JOINT_LEFT_MIDDLE_FINGER_PHALANX_INTERMEDIATE: 'int' = 36
    JOINT_LEFT_MIDDLE_FINGER_PHALANX_DISTAL: 'int' = 37
    JOINT_LEFT_MIDDLE_FINGER_TIP: 'int' = 38
    JOINT_LEFT_RING_FINGER_METACARPAL: 'int' = 39
    JOINT_LEFT_RING_FINGER_PHALANX_PROXIMAL: 'int' = 40
    JOINT_LEFT_RING_FINGER_PHALANX_INTERMEDIATE: 'int' = 41
    JOINT_LEFT_RING_FINGER_PHALANX_DISTAL: 'int' = 42
    JOINT_LEFT_RING_FINGER_TIP: 'int' = 43
    JOINT_LEFT_PINKY_FINGER_METACARPAL: 'int' = 44
    JOINT_LEFT_PINKY_FINGER_PHALANX_PROXIMAL: 'int' = 45
    JOINT_LEFT_PINKY_FINGER_PHALANX_INTERMEDIATE: 'int' = 46
    JOINT_LEFT_PINKY_FINGER_PHALANX_DISTAL: 'int' = 47
    JOINT_LEFT_PINKY_FINGER_TIP: 'int' = 48
    JOINT_RIGHT_HAND: 'int' = 49
    JOINT_RIGHT_PALM: 'int' = 50
    JOINT_RIGHT_WRIST: 'int' = 51
    JOINT_RIGHT_THUMB_METACARPAL: 'int' = 52
    JOINT_RIGHT_THUMB_PHALANX_PROXIMAL: 'int' = 53
    JOINT_RIGHT_THUMB_PHALANX_DISTAL: 'int' = 54
    JOINT_RIGHT_THUMB_TIP: 'int' = 55
    JOINT_RIGHT_INDEX_FINGER_METACARPAL: 'int' = 56
    JOINT_RIGHT_INDEX_FINGER_PHALANX_PROXIMAL: 'int' = 57
    JOINT_RIGHT_INDEX_FINGER_PHALANX_INTERMEDIATE: 'int' = 58
    JOINT_RIGHT_INDEX_FINGER_PHALANX_DISTAL: 'int' = 59
    JOINT_RIGHT_INDEX_FINGER_TIP: 'int' = 60
    JOINT_RIGHT_MIDDLE_FINGER_METACARPAL: 'int' = 61
    JOINT_RIGHT_MIDDLE_FINGER_PHALANX_PROXIMAL: 'int' = 62
    JOINT_RIGHT_MIDDLE_FINGER_PHALANX_INTERMEDIATE: 'int' = 63
    JOINT_RIGHT_MIDDLE_FINGER_PHALANX_DISTAL: 'int' = 64
    JOINT_RIGHT_MIDDLE_FINGER_TIP: 'int' = 65
    JOINT_RIGHT_RING_FINGER_METACARPAL: 'int' = 66
    JOINT_RIGHT_RING_FINGER_PHALANX_PROXIMAL: 'int' = 67
    JOINT_RIGHT_RING_FINGER_PHALANX_INTERMEDIATE: 'int' = 68
    JOINT_RIGHT_RING_FINGER_PHALANX_DISTAL: 'int' = 69
    JOINT_RIGHT_RING_FINGER_TIP: 'int' = 70
    JOINT_RIGHT_PINKY_FINGER_METACARPAL: 'int' = 71
    JOINT_RIGHT_PINKY_FINGER_PHALANX_PROXIMAL: 'int' = 72
    JOINT_RIGHT_PINKY_FINGER_PHALANX_INTERMEDIATE: 'int' = 73
    JOINT_RIGHT_PINKY_FINGER_PHALANX_DISTAL: 'int' = 74
    JOINT_RIGHT_PINKY_FINGER_TIP: 'int' = 75
    JOINT_MAX: 'int' = 76




class XRBodyTracker__JointFlags(Enum):

    JOINT_FLAG_ORIENTATION_VALID: 'int' = 1
    JOINT_FLAG_ORIENTATION_TRACKED: 'int' = 2
    JOINT_FLAG_POSITION_VALID: 'int' = 4
    JOINT_FLAG_POSITION_TRACKED: 'int' = 8




class XRFaceTracker__BlendShapeEntry(Enum):

    FT_EYE_LOOK_OUT_RIGHT: 'int' = 0
    FT_EYE_LOOK_IN_RIGHT: 'int' = 1
    FT_EYE_LOOK_UP_RIGHT: 'int' = 2
    FT_EYE_LOOK_DOWN_RIGHT: 'int' = 3
    FT_EYE_LOOK_OUT_LEFT: 'int' = 4
    FT_EYE_LOOK_IN_LEFT: 'int' = 5
    FT_EYE_LOOK_UP_LEFT: 'int' = 6
    FT_EYE_LOOK_DOWN_LEFT: 'int' = 7
    FT_EYE_CLOSED_RIGHT: 'int' = 8
    FT_EYE_CLOSED_LEFT: 'int' = 9
    FT_EYE_SQUINT_RIGHT: 'int' = 10
    FT_EYE_SQUINT_LEFT: 'int' = 11
    FT_EYE_WIDE_RIGHT: 'int' = 12
    FT_EYE_WIDE_LEFT: 'int' = 13
    FT_EYE_DILATION_RIGHT: 'int' = 14
    FT_EYE_DILATION_LEFT: 'int' = 15
    FT_EYE_CONSTRICT_RIGHT: 'int' = 16
    FT_EYE_CONSTRICT_LEFT: 'int' = 17
    FT_BROW_PINCH_RIGHT: 'int' = 18
    FT_BROW_PINCH_LEFT: 'int' = 19
    FT_BROW_LOWERER_RIGHT: 'int' = 20
    FT_BROW_LOWERER_LEFT: 'int' = 21
    FT_BROW_INNER_UP_RIGHT: 'int' = 22
    FT_BROW_INNER_UP_LEFT: 'int' = 23
    FT_BROW_OUTER_UP_RIGHT: 'int' = 24
    FT_BROW_OUTER_UP_LEFT: 'int' = 25
    FT_NOSE_SNEER_RIGHT: 'int' = 26
    FT_NOSE_SNEER_LEFT: 'int' = 27
    FT_NASAL_DILATION_RIGHT: 'int' = 28
    FT_NASAL_DILATION_LEFT: 'int' = 29
    FT_NASAL_CONSTRICT_RIGHT: 'int' = 30
    FT_NASAL_CONSTRICT_LEFT: 'int' = 31
    FT_CHEEK_SQUINT_RIGHT: 'int' = 32
    FT_CHEEK_SQUINT_LEFT: 'int' = 33
    FT_CHEEK_PUFF_RIGHT: 'int' = 34
    FT_CHEEK_PUFF_LEFT: 'int' = 35
    FT_CHEEK_SUCK_RIGHT: 'int' = 36
    FT_CHEEK_SUCK_LEFT: 'int' = 37
    FT_JAW_OPEN: 'int' = 38
    FT_MOUTH_CLOSED: 'int' = 39
    FT_JAW_RIGHT: 'int' = 40
    FT_JAW_LEFT: 'int' = 41
    FT_JAW_FORWARD: 'int' = 42
    FT_JAW_BACKWARD: 'int' = 43
    FT_JAW_CLENCH: 'int' = 44
    FT_JAW_MANDIBLE_RAISE: 'int' = 45
    FT_LIP_SUCK_UPPER_RIGHT: 'int' = 46
    FT_LIP_SUCK_UPPER_LEFT: 'int' = 47
    FT_LIP_SUCK_LOWER_RIGHT: 'int' = 48
    FT_LIP_SUCK_LOWER_LEFT: 'int' = 49
    FT_LIP_SUCK_CORNER_RIGHT: 'int' = 50
    FT_LIP_SUCK_CORNER_LEFT: 'int' = 51
    FT_LIP_FUNNEL_UPPER_RIGHT: 'int' = 52
    FT_LIP_FUNNEL_UPPER_LEFT: 'int' = 53
    FT_LIP_FUNNEL_LOWER_RIGHT: 'int' = 54
    FT_LIP_FUNNEL_LOWER_LEFT: 'int' = 55
    FT_LIP_PUCKER_UPPER_RIGHT: 'int' = 56
    FT_LIP_PUCKER_UPPER_LEFT: 'int' = 57
    FT_LIP_PUCKER_LOWER_RIGHT: 'int' = 58
    FT_LIP_PUCKER_LOWER_LEFT: 'int' = 59
    FT_MOUTH_UPPER_UP_RIGHT: 'int' = 60
    FT_MOUTH_UPPER_UP_LEFT: 'int' = 61
    FT_MOUTH_LOWER_DOWN_RIGHT: 'int' = 62
    FT_MOUTH_LOWER_DOWN_LEFT: 'int' = 63
    FT_MOUTH_UPPER_DEEPEN_RIGHT: 'int' = 64
    FT_MOUTH_UPPER_DEEPEN_LEFT: 'int' = 65
    FT_MOUTH_UPPER_RIGHT: 'int' = 66
    FT_MOUTH_UPPER_LEFT: 'int' = 67
    FT_MOUTH_LOWER_RIGHT: 'int' = 68
    FT_MOUTH_LOWER_LEFT: 'int' = 69
    FT_MOUTH_CORNER_PULL_RIGHT: 'int' = 70
    FT_MOUTH_CORNER_PULL_LEFT: 'int' = 71
    FT_MOUTH_CORNER_SLANT_RIGHT: 'int' = 72
    FT_MOUTH_CORNER_SLANT_LEFT: 'int' = 73
    FT_MOUTH_FROWN_RIGHT: 'int' = 74
    FT_MOUTH_FROWN_LEFT: 'int' = 75
    FT_MOUTH_STRETCH_RIGHT: 'int' = 76
    FT_MOUTH_STRETCH_LEFT: 'int' = 77
    FT_MOUTH_DIMPLE_RIGHT: 'int' = 78
    FT_MOUTH_DIMPLE_LEFT: 'int' = 79
    FT_MOUTH_RAISER_UPPER: 'int' = 80
    FT_MOUTH_RAISER_LOWER: 'int' = 81
    FT_MOUTH_PRESS_RIGHT: 'int' = 82
    FT_MOUTH_PRESS_LEFT: 'int' = 83
    FT_MOUTH_TIGHTENER_RIGHT: 'int' = 84
    FT_MOUTH_TIGHTENER_LEFT: 'int' = 85
    FT_TONGUE_OUT: 'int' = 86
    FT_TONGUE_UP: 'int' = 87
    FT_TONGUE_DOWN: 'int' = 88
    FT_TONGUE_RIGHT: 'int' = 89
    FT_TONGUE_LEFT: 'int' = 90
    FT_TONGUE_ROLL: 'int' = 91
    FT_TONGUE_BLEND_DOWN: 'int' = 92
    FT_TONGUE_CURL_UP: 'int' = 93
    FT_TONGUE_SQUISH: 'int' = 94
    FT_TONGUE_FLAT: 'int' = 95
    FT_TONGUE_TWIST_RIGHT: 'int' = 96
    FT_TONGUE_TWIST_LEFT: 'int' = 97
    FT_SOFT_PALATE_CLOSE: 'int' = 98
    FT_THROAT_SWALLOW: 'int' = 99
    FT_NECK_FLEX_RIGHT: 'int' = 100
    FT_NECK_FLEX_LEFT: 'int' = 101
    FT_EYE_CLOSED: 'int' = 102
    FT_EYE_WIDE: 'int' = 103
    FT_EYE_SQUINT: 'int' = 104
    FT_EYE_DILATION: 'int' = 105
    FT_EYE_CONSTRICT: 'int' = 106
    FT_BROW_DOWN_RIGHT: 'int' = 107
    FT_BROW_DOWN_LEFT: 'int' = 108
    FT_BROW_DOWN: 'int' = 109
    FT_BROW_UP_RIGHT: 'int' = 110
    FT_BROW_UP_LEFT: 'int' = 111
    FT_BROW_UP: 'int' = 112
    FT_NOSE_SNEER: 'int' = 113
    FT_NASAL_DILATION: 'int' = 114
    FT_NASAL_CONSTRICT: 'int' = 115
    FT_CHEEK_PUFF: 'int' = 116
    FT_CHEEK_SUCK: 'int' = 117
    FT_CHEEK_SQUINT: 'int' = 118
    FT_LIP_SUCK_UPPER: 'int' = 119
    FT_LIP_SUCK_LOWER: 'int' = 120
    FT_LIP_SUCK: 'int' = 121
    FT_LIP_FUNNEL_UPPER: 'int' = 122
    FT_LIP_FUNNEL_LOWER: 'int' = 123
    FT_LIP_FUNNEL: 'int' = 124
    FT_LIP_PUCKER_UPPER: 'int' = 125
    FT_LIP_PUCKER_LOWER: 'int' = 126
    FT_LIP_PUCKER: 'int' = 127
    FT_MOUTH_UPPER_UP: 'int' = 128
    FT_MOUTH_LOWER_DOWN: 'int' = 129
    FT_MOUTH_OPEN: 'int' = 130
    FT_MOUTH_RIGHT: 'int' = 131
    FT_MOUTH_LEFT: 'int' = 132
    FT_MOUTH_SMILE_RIGHT: 'int' = 133
    FT_MOUTH_SMILE_LEFT: 'int' = 134
    FT_MOUTH_SMILE: 'int' = 135
    FT_MOUTH_SAD_RIGHT: 'int' = 136
    FT_MOUTH_SAD_LEFT: 'int' = 137
    FT_MOUTH_SAD: 'int' = 138
    FT_MOUTH_STRETCH: 'int' = 139
    FT_MOUTH_DIMPLE: 'int' = 140
    FT_MOUTH_TIGHTENER: 'int' = 141
    FT_MOUTH_PRESS: 'int' = 142
    FT_MAX: 'int' = 143




class XRHandModifier3D__BoneUpdate(Enum):

    BONE_UPDATE_FULL: 'int' = 0
    BONE_UPDATE_ROTATION_ONLY: 'int' = 1
    BONE_UPDATE_MAX: 'int' = 2




class XRHandTracker__HandTrackingSource(Enum):

    HAND_TRACKING_SOURCE_UNKNOWN: 'int' = 0
    HAND_TRACKING_SOURCE_UNOBSTRUCTED: 'int' = 1
    HAND_TRACKING_SOURCE_CONTROLLER: 'int' = 2
    HAND_TRACKING_SOURCE_NOT_TRACKED: 'int' = 3
    HAND_TRACKING_SOURCE_MAX: 'int' = 4




class XRHandTracker__HandJoint(Enum):

    HAND_JOINT_PALM: 'int' = 0
    HAND_JOINT_WRIST: 'int' = 1
    HAND_JOINT_THUMB_METACARPAL: 'int' = 2
    HAND_JOINT_THUMB_PHALANX_PROXIMAL: 'int' = 3
    HAND_JOINT_THUMB_PHALANX_DISTAL: 'int' = 4
    HAND_JOINT_THUMB_TIP: 'int' = 5
    HAND_JOINT_INDEX_FINGER_METACARPAL: 'int' = 6
    HAND_JOINT_INDEX_FINGER_PHALANX_PROXIMAL: 'int' = 7
    HAND_JOINT_INDEX_FINGER_PHALANX_INTERMEDIATE: 'int' = 8
    HAND_JOINT_INDEX_FINGER_PHALANX_DISTAL: 'int' = 9
    HAND_JOINT_INDEX_FINGER_TIP: 'int' = 10
    HAND_JOINT_MIDDLE_FINGER_METACARPAL: 'int' = 11
    HAND_JOINT_MIDDLE_FINGER_PHALANX_PROXIMAL: 'int' = 12
    HAND_JOINT_MIDDLE_FINGER_PHALANX_INTERMEDIATE: 'int' = 13
    HAND_JOINT_MIDDLE_FINGER_PHALANX_DISTAL: 'int' = 14
    HAND_JOINT_MIDDLE_FINGER_TIP: 'int' = 15
    HAND_JOINT_RING_FINGER_METACARPAL: 'int' = 16
    HAND_JOINT_RING_FINGER_PHALANX_PROXIMAL: 'int' = 17
    HAND_JOINT_RING_FINGER_PHALANX_INTERMEDIATE: 'int' = 18
    HAND_JOINT_RING_FINGER_PHALANX_DISTAL: 'int' = 19
    HAND_JOINT_RING_FINGER_TIP: 'int' = 20
    HAND_JOINT_PINKY_FINGER_METACARPAL: 'int' = 21
    HAND_JOINT_PINKY_FINGER_PHALANX_PROXIMAL: 'int' = 22
    HAND_JOINT_PINKY_FINGER_PHALANX_INTERMEDIATE: 'int' = 23
    HAND_JOINT_PINKY_FINGER_PHALANX_DISTAL: 'int' = 24
    HAND_JOINT_PINKY_FINGER_TIP: 'int' = 25
    HAND_JOINT_MAX: 'int' = 26




class XRHandTracker__HandJointFlags(Enum):

    HAND_JOINT_FLAG_ORIENTATION_VALID: 'int' = 1
    HAND_JOINT_FLAG_ORIENTATION_TRACKED: 'int' = 2
    HAND_JOINT_FLAG_POSITION_VALID: 'int' = 4
    HAND_JOINT_FLAG_POSITION_TRACKED: 'int' = 8
    HAND_JOINT_FLAG_LINEAR_VELOCITY_VALID: 'int' = 16
    HAND_JOINT_FLAG_ANGULAR_VELOCITY_VALID: 'int' = 32




class XRInterface__Capabilities(Enum):

    XR_NONE: 'int' = 0
    XR_MONO: 'int' = 1
    XR_STEREO: 'int' = 2
    XR_QUAD: 'int' = 4
    XR_VR: 'int' = 8
    XR_AR: 'int' = 16
    XR_EXTERNAL: 'int' = 32




class XRInterface__TrackingStatus(Enum):

    XR_NORMAL_TRACKING: 'int' = 0
    XR_EXCESSIVE_MOTION: 'int' = 1
    XR_INSUFFICIENT_FEATURES: 'int' = 2
    XR_UNKNOWN_TRACKING: 'int' = 3
    XR_NOT_TRACKING: 'int' = 4




class XRInterface__PlayAreaMode(Enum):

    XR_PLAY_AREA_UNKNOWN: 'int' = 0
    XR_PLAY_AREA_3DOF: 'int' = 1
    XR_PLAY_AREA_SITTING: 'int' = 2
    XR_PLAY_AREA_ROOMSCALE: 'int' = 3
    XR_PLAY_AREA_STAGE: 'int' = 4




class XRInterface__EnvironmentBlendMode(Enum):

    XR_ENV_BLEND_MODE_OPAQUE: 'int' = 0
    XR_ENV_BLEND_MODE_ADDITIVE: 'int' = 1
    XR_ENV_BLEND_MODE_ALPHA_BLEND: 'int' = 2




class XRPose__TrackingConfidence(Enum):

    XR_TRACKING_CONFIDENCE_NONE: 'int' = 0
    XR_TRACKING_CONFIDENCE_LOW: 'int' = 1
    XR_TRACKING_CONFIDENCE_HIGH: 'int' = 2




class XRPositionalTracker__TrackerHand(Enum):

    TRACKER_HAND_UNKNOWN: 'int' = 0
    TRACKER_HAND_LEFT: 'int' = 1
    TRACKER_HAND_RIGHT: 'int' = 2
    TRACKER_HAND_MAX: 'int' = 3




class XRServer__TrackerType(Enum):

    TRACKER_HEAD: 'int' = 1
    TRACKER_CONTROLLER: 'int' = 2
    TRACKER_BASESTATION: 'int' = 4
    TRACKER_ANCHOR: 'int' = 8
    TRACKER_HAND: 'int' = 16
    TRACKER_BODY: 'int' = 32
    TRACKER_FACE: 'int' = 64
    TRACKER_ANY_KNOWN: 'int' = 127
    TRACKER_UNKNOWN: 'int' = 128
    TRACKER_ANY: 'int' = 255




class XRServer__RotationMode(Enum):

    RESET_FULL_ROTATION: 'int' = 0
    RESET_BUT_KEEP_TILT: 'int' = 1
    DONT_RESET_ROTATION: 'int' = 2




class ZIPPacker__ZipAppend(Enum):

    APPEND_CREATE: 'int' = 0
    APPEND_CREATEAFTER: 'int' = 1
    APPEND_ADDINZIP: 'int' = 2




class Vector2__Axis(Enum):

    AXIS_X: 'int' = 0
    AXIS_Y: 'int' = 1




class Vector2i__Axis(Enum):

    AXIS_X: 'int' = 0
    AXIS_Y: 'int' = 1




class Vector3__Axis(Enum):

    AXIS_X: 'int' = 0
    AXIS_Y: 'int' = 1
    AXIS_Z: 'int' = 2




class Vector3i__Axis(Enum):

    AXIS_X: 'int' = 0
    AXIS_Y: 'int' = 1
    AXIS_Z: 'int' = 2




class Vector4__Axis(Enum):

    AXIS_X: 'int' = 0
    AXIS_Y: 'int' = 1
    AXIS_Z: 'int' = 2
    AXIS_W: 'int' = 3




class Vector4i__Axis(Enum):

    AXIS_X: 'int' = 0
    AXIS_Y: 'int' = 1
    AXIS_Z: 'int' = 2
    AXIS_W: 'int' = 3




class Projection__Planes(Enum):

    PLANE_NEAR: 'int' = 0
    PLANE_FAR: 'int' = 1
    PLANE_LEFT: 'int' = 2
    PLANE_TOP: 'int' = 3
    PLANE_RIGHT: 'int' = 4
    PLANE_BOTTOM: 'int' = 5




class Vector2__Axis(Enum):

    AXIS_X: 'int' = 0
    AXIS_Y: 'int' = 1




class Vector2i__Axis(Enum):

    AXIS_X: 'int' = 0
    AXIS_Y: 'int' = 1




class Vector3__Axis(Enum):

    AXIS_X: 'int' = 0
    AXIS_Y: 'int' = 1
    AXIS_Z: 'int' = 2




class Vector3i__Axis(Enum):

    AXIS_X: 'int' = 0
    AXIS_Y: 'int' = 1
    AXIS_Z: 'int' = 2




class Vector4__Axis(Enum):

    AXIS_X: 'int' = 0
    AXIS_Y: 'int' = 1
    AXIS_Z: 'int' = 2
    AXIS_W: 'int' = 3




class Vector4i__Axis(Enum):

    AXIS_X: 'int' = 0
    AXIS_Y: 'int' = 1
    AXIS_Z: 'int' = 2
    AXIS_W: 'int' = 3




class Projection__Planes(Enum):

    PLANE_NEAR: 'int' = 0
    PLANE_FAR: 'int' = 1
    PLANE_LEFT: 'int' = 2
    PLANE_TOP: 'int' = 3
    PLANE_RIGHT: 'int' = 4
    PLANE_BOTTOM: 'int' = 5



