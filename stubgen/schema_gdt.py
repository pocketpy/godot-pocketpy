from dataclasses import dataclass, field, asdict
import json
# This is a script of converting godot extension api into dataclass.
# In this file, @dataclass is used to storage the info. The 
# corresponding source code is linked with a permalink before 
# each dataclass.
# How does godot's source code work:
# A "Dictionary" class is used. A empty dictionary, for example, 
# `Dictionary header`, set the "version_major" by 
# `header["version_major"] = 4`, the output of header will be
# "header": {"version_major": 4}. Subsequently added attributes
#  will be arranged in order. So "version_minor" is always behind 
# the "version_major".
# A "Array" class is used. Array contains "Dictionary" classes. 
# For example, in "builtin_class_sizes", "sizes" has output:
# "sizes: [{dict1}, {dict2}, ...]", the "Array sizes" contains 
# dict1, dict2, ...
# Dict may contains Array. 
# With the above 2 classes, godot outputs json following the source 
# code's logic. 


# https://github.com/godotengine/godot/blob/1b37dacc1842779fb0d03a5b09026f59c13744fc/core/extension/extension_api_dump.cpp#L106
# Header is defined here, but L120-L124 has a key "precision" added,
# so "precision" is also added here
@dataclass
class Header:
    version_major: int
    version_minor: int
    version_patch: int
    version_status: str
    version_build: str
    version_full_name: str
    precision: str
# https://github.com/godotengine/godot/blob/1b37dacc1842779fb0d03a5b09026f59c13744fc/core/extension/extension_api_dump.cpp#L254
# dict in "sizes"    
# It's storaged in `Dictionary d2`, each d2 has "name" and "size" attributes
@dataclass
class TypeSize:
    name: str
    size: int
# https://github.com/godotengine/godot/blob/1b37dacc1842779fb0d03a5b09026f59c13744fc/core/extension/extension_api_dump.cpp#L249
# build_configuration, and array of type sizes
# There are 4 kinds of "build_configuration" for "builtin_class_sizes"
@dataclass
class TypeBuildConfiguration:
    build_configuration: str
    sizes: list[TypeSize] = field(default_factory=list)
# https://github.com/godotengine/godot/blob/1b37dacc1842779fb0d03a5b09026f59c13744fc/core/extension/extension_api_dump.cpp#L277
# core_type_sizes
# creating an Array containing all "build_configuration" and their sizes    
@dataclass
class BuiltinClassSizes:
    builtin_class_sizes: list[TypeBuildConfiguration] = field(default_factory=list)
# https://github.com/godotengine/godot/blob/1b37dacc1842779fb0d03a5b09026f59c13744fc/core/extension/extension_api_dump.cpp#L449
# member and their offset properties
# `Dictionary d3` containing these info is part of `Array members`
@dataclass
class MemberOffset:
    member: str
    offset: int
    meta: str
# https://github.com/godotengine/godot/blob/1b37dacc1842779fb0d03a5b09026f59c13744fc/core/extension/extension_api_dump.cpp#L444
# `Array members`, and class name
# the array that contains `Dictionary d3` with members' info, the name indicates 
# the class, for example, `vector2` under float_32 configuration, has 2 members 
# `x` and `y` in the array, and `y` is after `x`, making y's offset is 
# 1 float_32(4 bytes).
@dataclass
class ClassMember:
    name: str
    members: list[MemberOffset] = field(default_factory=list)
# https://github.com/godotengine/godot/blob/1b37dacc1842779fb0d03a5b09026f59c13744fc/core/extension/extension_api_dump.cpp#L420
# build_configuration, and all the classes under this configuration
# the classes are arrays containing name, member offset info
@dataclass
class OffsetBuildConfiguration:
    build_configuration: str
    classes: list[ClassMember] = field(default_factory=list)
# https://github.com/godotengine/godot/blob/1b37dacc1842779fb0d03a5b09026f59c13744fc/core/extension/extension_api_dump.cpp#L478
# core_type_member_offsets
# an array with all build_configurations and their classes
@dataclass
class BuiltinClassMemberOffsets:
    builtin_class_member_offsets: list[OffsetBuildConfiguration] = field(default_factory=list)
# https://github.com/godotengine/godot/blob/1b37dacc1842779fb0d03a5b09026f59c13744fc/core/extension/extension_api_dump.cpp#L508
# global constant's info
# L505,L506 shows that the code block processes global enums and 
# constants together. If one has enum name, it will be in the "global_enums"
@dataclass
class GlobalConstant:
    name: str
    value: int
    is_bitfield: bool
    description: str | None
# https://github.com/godotengine/godot/blob/1b37dacc1842779fb0d03a5b09026f59c13744fc/core/extension/extension_api_dump.cpp#L520
# constants
# array of global constants
@dataclass
class GlobalConstants:
    global_constants: list[GlobalConstant] = field(default_factory=list)
# https://github.com/godotengine/godot/blob/1b37dacc1842779fb0d03a5b09026f59c13744fc/core/extension/extension_api_dump.cpp#L539
# name and value of enum values
# for example, "Side" has "top, bottom, left, right", properties 
# here indicates the value of "SIDE_TOP", ...
@dataclass
class EnumValues:
    name: str
    value: int
    description: str | None
# https://github.com/godotengine/godot/blob/1b37dacc1842779fb0d03a5b09026f59c13744fc/core/extension/extension_api_dump.cpp#L528
# name and other properties of an enum
# values contains the exact values of the current enum
@dataclass
class GlobalEnum:
    name: str
    is_bitfield: bool
    description: str | None
    values: list[EnumValues] = field(default_factory=list)
# https://github.com/godotengine/godot/blob/1b37dacc1842779fb0d03a5b09026f59c13744fc/core/extension/extension_api_dump.cpp#L553
# enums
# an array contains all the enums
@dataclass
class GlobalEnums:
    global_enums: list[GlobalEnum] = field(default_factory=list)
# https://github.com/godotengine/godot/blob/1b37dacc1842779fb0d03a5b09026f59c13744fc/core/extension/extension_api_dump.cpp#L594
# argument name and its type
# 
@dataclass
class UtilityArguments:
    name: str
    type: str
# https://github.com/godotengine/godot/blob/1b37dacc1842779fb0d03a5b09026f59c13744fc/core/extension/extension_api_dump.cpp#L571
# function's properties
# include basic properties of a functin. Array arguments contains 
# the arguments it needs.    
@dataclass
class UtilityFunction:
    name: str
    return_type: str | None
    category: str
    is_vararg: bool
    hash: int
    arguments: list[UtilityArguments] | None = field(default_factory=list)
    description: str | None = field(default=None)
# https://github.com/godotengine/godot/blob/1b37dacc1842779fb0d03a5b09026f59c13744fc/core/extension/extension_api_dump.cpp#L615
# utility_funs
# contains all the utility functions    
@dataclass
class UtilityFunctions:
    utility_functions: list[UtilityFunction] = field(default_factory=list)
# https://github.com/godotengine/godot/blob/1b37dacc1842779fb0d03a5b09026f59c13744fc/core/extension/extension_api_dump.cpp#L754
# operator of the class
# contains basic info of the operator
@dataclass
class BuiltinClassOperator:
    name: str
    right_type: str
    return_type: bool
    description: str | None
# https://github.com/godotengine/godot/blob/1b37dacc1842779fb0d03a5b09026f59c13744fc/core/extension/extension_api_dump.cpp#L654
# a member of the class    
# contains basic info of the member
@dataclass
class BuiltinClassMember:
    name: str
    type: str
    description: str | None
# https://github.com/godotengine/godot/blob/1b37dacc1842779fb0d03a5b09026f59c13744fc/core/extension/extension_api_dump.cpp#L678
# a constant of the class
# contains basic info of the constant    
@dataclass
class BuiltinClassConstant:
    name: str
    type: str
    value: str
    description: str | None
# https://github.com/godotengine/godot/blob/1b37dacc1842779fb0d03a5b09026f59c13744fc/core/extension/extension_api_dump.cpp#L713
# name and value of enum values
#    
@dataclass
class BuiltinClassEnumValue:
    name: str
    value: int
    description: str | None
# https://github.com/godotengine/godot/blob/1b37dacc1842779fb0d03a5b09026f59c13744fc/core/extension/extension_api_dump.cpp#L704
# name and other properties of an enum
#     
@dataclass
class BuiltinClassEnum:
    name: str
    description: str | None
    values: list[BuiltinClassEnumValue] | None= field(default_factory=list)
# https://github.com/godotengine/godot/blob/1b37dacc1842779fb0d03a5b09026f59c13744fc/core/extension/extension_api_dump.cpp#L805
# argument's name, type, (perhaps with a default value) of the method
#     
@dataclass
class BuiltinClassMehodArgument:
    name: str
    type: str
    default_value: str | None
# https://github.com/godotengine/godot/blob/1b37dacc1842779fb0d03a5b09026f59c13744fc/core/extension/extension_api_dump.cpp#L789
# a method for the builtin class
# contains properties of the method    
@dataclass
class BuiltinClassMethod:
    name: str
    return_type: str | None
    is_vararg: bool
    is_const: bool
    is_static: bool
    hash: int
    arguments: list[BuiltinClassMehodArgument] | None = field(default_factory=list)
    description: str | None = field(default=None)
# https://github.com/godotengine/godot/blob/1b37dacc1842779fb0d03a5b09026f59c13744fc/core/extension/extension_api_dump.cpp#L846
# argument of the constructor
#     
@dataclass
class BuiltinClassConstructorArgument:
    name: str
    type: str
# https://github.com/godotengine/godot/blob/1b37dacc1842779fb0d03a5b09026f59c13744fc/core/extension/extension_api_dump.cpp#L840
# a constructor of the builtin class
# contains properties of the constructor    
@dataclass
class BuiltinClassConstructor:
    index: int
    arguments: list[BuiltinClassConstructorArgument] | None = field(default_factory=list)
    description: str | None = field(default=None)
# https://github.com/godotengine/godot/blob/1b37dacc1842779fb0d03a5b09026f59c13744fc/core/extension/extension_api_dump.cpp#L633
# a class's basic properties
#     
@dataclass
class BuiltinClass:
    name: str
    indexing_return_type: str | None
    is_keyed: bool
    members: list[BuiltinClassMember] | None = field(default_factory=list)
    constants: list[BuiltinClassConstant] | None = field(default_factory=list)
    enums: list[BuiltinClassEnum] | None = field(default_factory=list)
    operators: list[BuiltinClassOperator] = field(default_factory=list)
    methods: list[BuiltinClassMethod] | None = field(default_factory=list)
    constructors: list[BuiltinClassConstructor] = field(default_factory=list)
    has_destructor: bool = field(default=False)
    brief_description: str | None = field(default=None)
    description: str | None = field(default=None)
# https://github.com/godotengine/godot/blob/1b37dacc1842779fb0d03a5b09026f59c13744fc/core/extension/extension_api_dump.cpp#L893
# builtins
# contains all the builtin classes    
@dataclass
class BuiltinClasses:
    builtin_classes: list[BuiltinClass] = field(default_factory=list)
# https://github.com/godotengine/godot/blob/1b37dacc1842779fb0d03a5b09026f59c13744fc/core/extension/extension_api_dump.cpp#L979
# an enum's properties of the current class
# contains name and value
@dataclass
class ClassesEnumValue:
    name: str
    value: int
    description: str | None
# https://github.com/godotengine/godot/blob/1b37dacc1842779fb0d03a5b09026f59c13744fc/core/extension/extension_api_dump.cpp#L971
# an enum of the class
# contains its name, an array of values
@dataclass
class ClassesEnum:
    name: str
    is_bitfield: bool
    values: list[ClassesEnumValue] | None = field(default_factory=list)
    description: str | None = field(default=None)
# https://github.com/godotengine/godot/blob/1b37dacc1842779fb0d03a5b09026f59c13744fc/core/extension/extension_api_dump.cpp#L945
# a constant of the class
#
@dataclass
class ClassesConstant:
    name: str
    value: int
    description: str | None
# https://github.com/godotengine/godot/blob/1b37dacc1842779fb0d03a5b09026f59c13744fc/core/extension/extension_api_dump.cpp#L1044
# https://github.com/godotengine/godot/blob/1b37dacc1842779fb0d03a5b09026f59c13744fc/core/extension/extension_api_dump.cpp#L1142
# method's return value
# for virtual methods, L1044, it depends on "has_return"
# for not virtual, not hidden methods, it's decided by "i"'s value, 
# but be careful, whether a method has return value is 
# still decided by "has_return()", so here are no big 
# difference between virtual and other methods' json
@dataclass
class ClassesMethodReturnValue:
    type: str
    meta: str | None
# https://github.com/godotengine/godot/blob/1b37dacc1842779fb0d03a5b09026f59c13744fc/core/extension/extension_api_dump.cpp#L1058
# https://github.com/godotengine/godot/blob/1b37dacc1842779fb0d03a5b09026f59c13744fc/core/extension/extension_api_dump.cpp#L1144
# method's argument
# similiar to method's return value, both virtual and 
# other methods' argument has name, type, meta, default_value    
@dataclass
class ClassesMethodArgument:
    name: str
    type: str
    meta: str | None
    default_value: str | None
# https://github.com/godotengine/godot/blob/1b37dacc1842779fb0d03a5b09026f59c13744fc/core/extension/extension_api_dump.cpp#L1018
# Virtual method's properties
#     
@dataclass
class ClassesMethodVirtual:
    name: str
    is_const: bool
    is_static: bool
    is_required: bool | None
    is_vararg: bool
    is_virtual: bool
    hash: int
    hash_compatibility: list[int] | None = field(default_factory=list)
    return_value: ClassesMethodReturnValue | None = field(default_factory=dict) # type: ignore
    arguments: list[ClassesMethodArgument] | None = field(default_factory=list)
    description: str | None = field(default=None)
# https://github.com/godotengine/godot/blob/1b37dacc1842779fb0d03a5b09026f59c13744fc/core/extension/extension_api_dump.cpp#L1090
# not virtual, not hidden methods
# 
@dataclass
class ClassesMethod:
    name: str
    is_const: bool
    is_vararg: bool
    is_static: bool
    is_virtual: bool
    hash: int
    hash_compatibility: list[int] | None = field(default_factory=list)
    return_value: ClassesMethodReturnValue | None = field(default_factory=dict) # type: ignore
    arguments: list[ClassesMethodArgument] | None = field(default_factory=list)    
    description: str | None = field(default=None)
# https://github.com/godotengine/godot/blob/1b37dacc1842779fb0d03a5b09026f59c13744fc/core/extension/extension_api_dump.cpp#L1183
# argument of class's signal property
# includes name, type, may have meta
@dataclass
class ClassesSignalArgument:
    name: str
    type: str
    meta: str | None
# https://github.com/godotengine/godot/blob/1b37dacc1842779fb0d03a5b09026f59c13744fc/core/extension/extension_api_dump.cpp#L1204
# signal of the class
# contains name and an array of arguments    
@dataclass
class ClassesSignal:
    name: str
    arguments: list[ClassesSignalArgument] | None = field(default_factory=list)
    description: str | None = field(default=None)
# https://github.com/godotengine/godot/blob/1b37dacc1842779fb0d03a5b09026f59c13744fc/core/extension/extension_api_dump.cpp#L1253
# property of the class
# 
@dataclass
class ClassesProperty:
    type: str
    name: str
    setter: str | None
    getter: str | None
    index: str | None
    description: str | None
# https://github.com/godotengine/godot/blob/1b37dacc1842779fb0d03a5b09026f59c13744fc/core/extension/extension_api_dump.cpp#L913
# a single class's property
#     
@dataclass
class ClassesSingle:
    name: str
    is_refcounted: bool
    is_instantiable: bool
    inherits: str | None
    api_type: str
    constants: list[ClassesConstant] | None = field(default_factory=list)
    enums: list[ClassesEnum] | None = field(default_factory=list)
    methods: list[ClassesMethod] | list[ClassesMethodVirtual] | None = field(default_factory=list)
    signals: list[ClassesSignal] | None = field(default_factory=list)
    properties: list[ClassesProperty] | None = field(default_factory=list)
    brief_description: str | None = field(default=None)
    description: str | None = field(default=None)
# https://github.com/godotengine/godot/blob/1b37dacc1842779fb0d03a5b09026f59c13744fc/core/extension/extension_api_dump.cpp#L1266
# contains all the classes
# 
@dataclass
class Classes:
    classes: list[ClassesSingle] = field(default_factory=list)
# https://github.com/godotengine/godot/blob/1b37dacc1842779fb0d03a5b09026f59c13744fc/core/extension/extension_api_dump.cpp#L1280
# singleton's name and type
# 
@dataclass
class Singleton:
    name: str
    type: str
# https://github.com/godotengine/godot/blob/1b37dacc1842779fb0d03a5b09026f59c13744fc/core/extension/extension_api_dump.cpp#L1287
# an array contains singletons
# 
@dataclass
class Singletons:
    singletons: list[Singleton] = field(default_factory=list)
# https://github.com/godotengine/godot/blob/1b37dacc1842779fb0d03a5b09026f59c13744fc/core/extension/extension_api_dump.cpp#L1305
# native structure's name and format
#     
@dataclass
class NativeStructure:
    name: str
    format: str
# https://github.com/godotengine/godot/blob/1b37dacc1842779fb0d03a5b09026f59c13744fc/core/extension/extension_api_dump.cpp#L1309
# an array contains native structures    
@dataclass
class NativeStructures:
    native_structures: list[NativeStructure] = field(default_factory=list)

@dataclass
class GodotInOne:
    header: Header
    builtin_class_sizes: list[TypeBuildConfiguration] = field(default_factory=list)
    builtin_class_member_offsets: list[OffsetBuildConfiguration] = field(default_factory=list)
    global_constants: list[GlobalConstant] = field(default_factory=list)
    global_enums: list[GlobalEnum] = field(default_factory=list)
    utility_functions: list[UtilityFunction] = field(default_factory=list)
    builtin_classes: list[BuiltinClass] = field(default_factory=list)
    classes: list[ClassesSingle] = field(default_factory=list)
    singletons: list[Singleton] = field(default_factory=list)
    native_structures: list[NativeStructure] = field(default_factory=list)
    

def parse_builtin_class_sizes(json_data: dict) -> BuiltinClassSizes:
    build_configurations = []
    for config in json_data.get('builtin_class_sizes', []):
        sizes = [TypeSize(name=size_info['name'], size=size_info['size']) for size_info in config.get('sizes', [])]
        build_configuration = TypeBuildConfiguration(
            build_configuration=config.get('build_configuration'),
            sizes=sizes
        )
        build_configurations.append(build_configuration)

    return BuiltinClassSizes(builtin_class_sizes=build_configurations)

def parse_builtin_class_member_offsets(json_data: dict) -> BuiltinClassMemberOffsets:
    build_configurations = []
    for config in json_data.get('builtin_class_member_offsets', []):
        config_classes = []
        for classes in config.get('classes', []):
            members = [MemberOffset(member=member['member'],
                                    offset=member['offset'],
                                    meta=member['meta']) 
                       for member in classes.get('members', [])]
            config_classes.append(ClassMember(name=classes['name'],
                                              members=members))
        build_configurations.append(OffsetBuildConfiguration(build_configuration=config['build_configuration'],
                                                             classes=config_classes))
    return BuiltinClassMemberOffsets(builtin_class_member_offsets=build_configurations)

def parse_global_constants(json_data: dict) -> GlobalConstants:
    constants = []
    for constant in json_data.get('global_constants', []):
        constants.append(GlobalConstant(name=constant['name'],
                                        value=constant['value'],
                                        is_bitfield=constant['is_bitfield'],
                                        description=constant.get('description')))
    return GlobalConstants(global_constants=constants)
            
def parse_global_enums(json_data: dict) -> GlobalEnums:
    enums = []
    for enum in json_data.get('global_enums', []):
        values = [EnumValues(name=enum_value['name'],
                             value=enum_value['value'],
                             description=enum_value.get('description'))
                  for enum_value in enum.get('values')]
        enums.append(GlobalEnum(name=enum['name'],
                                is_bitfield=enum['is_bitfield'],
                                values=values,
                                description=enum.get('description')))
    return GlobalEnums(global_enums=enums)
            
def parse_utility_functions(json_data: dict) -> UtilityFunctions:
    utility_functions = []
    for func in json_data.get('utility_functions', []):
        arg_list = func.get('arguments', [])
        arguments = [UtilityArguments(name=arg['name'],
                                        type=arg['type'])
                    for arg in arg_list]
        if not arguments:
            arguments = None
        utility_functions.append(UtilityFunction(name=func['name'],
                                                 return_type=func.get('return_type'),
                                                 category=func['category'],
                                                 is_vararg=func['is_vararg'],
                                                 hash=func['hash'],
                                                 arguments=arguments,
                                                 description=func.get('description')))
    return UtilityFunctions(utility_functions=utility_functions)
   
def parse_builtin_classes(json_data: dict) -> BuiltinClasses:
    builtin_classes = []
    for builtin_class in json_data.get('builtin_classes', []):
        operators = [BuiltinClassOperator(name=operator['name'],
                                   right_type=operator.get('right_type'),
                                   return_type=operator['return_type'],
                                   description=operator.get('description'))
                  for operator in builtin_class.get('operators')]
        builtin_constructors = []
        for builtin_constructor in builtin_class.get('constructors', []):
            arg_list = builtin_constructor.get('arguments', [])
            arguments = [BuiltinClassConstructorArgument(name=arg['name'],
                                                         type=arg['type'])
                         for arg in arg_list]
            if not arguments:
                arguments = None
            constructor = BuiltinClassConstructor(index=builtin_constructor['index'],
                                                  arguments=arguments,
                                                  description=builtin_constructor.get('description'))
            builtin_constructors.append(constructor)
        member_list = builtin_class.get('members', [])
        members = [BuiltinClassMember(name=memb['name'],
                                      type=memb['type'],
                                      description=memb.get('description'))
                   for memb in member_list]
        if not members:
            members = None
        constant_list = builtin_class.get('constants', [])
        constants = [BuiltinClassConstant(name=const['name'],
                                          type=const['type'],
                                          value=const['value'],
                                          description=const.get('description'))
                     for const in constant_list]
        if not constants:
            constants = None
        builtin_enums = []
        for builtin_enum in builtin_class.get('enums', []):
            enum_values = [BuiltinClassEnumValue(name=value['name'],
                                                value=value['value'],
                                                description=value.get('description'))
                          for value in builtin_enum.get('values', [])]
            if not enum_values:
                enum_values = None
            enum = BuiltinClassEnum(name=builtin_enum['name'],
                                    values=enum_values,
                                    description=builtin_enum.get('description'))
            builtin_enums.append(enum)
        if not builtin_enums:
            builtin_enums = None
        builtin_methods = []
        for builtin_method in builtin_class.get('methods', []):
            method_arguments = [BuiltinClassMehodArgument(name=arg['name'],
                                                          type=arg['type'],
                                                          default_value=arg.get('default_value'))
                                for arg in builtin_method.get('arguments', [])]
            if not method_arguments:
                method_arguments = None
            method = BuiltinClassMethod(name=builtin_method['name'],
                                        return_type=builtin_method.get('return_type'),
                                        is_vararg=builtin_method['is_vararg'],
                                        is_const=builtin_method['is_const'],
                                        is_static=builtin_method['is_static'],
                                        hash=builtin_method['hash'],
                                        arguments=method_arguments,
                                        description=builtin_method.get('description'))
            builtin_methods.append(method)
        if not builtin_methods:
            builtin_methods = None
        builtin_classes.append(BuiltinClass(name=builtin_class['name'],
                                            is_keyed=builtin_class['is_keyed'],
                                            indexing_return_type=builtin_class.get('indexing_return_type'),
                                            has_destructor=builtin_class['has_destructor'],
                                            members=members,
                                            constants=constants,
                                            enums=builtin_enums,
                                            methods=builtin_methods,
                                            constructors=builtin_constructors,
                                            operators=operators,
                                            description=builtin_class.get('description'),
                                            brief_description=builtin_class.get('brief_description')))
    return BuiltinClasses(builtin_classes=builtin_classes)
     
def parse_classes(json_data: dict) -> Classes:
    classes = []
    for classes_single in json_data.get('classes', []):
        classes_enums = []
        for classes_enum in classes_single.get('enums', []):
            value_list = classes_enum.get('values', [])
            values = [ClassesEnumValue(name=value['name'],
                                       value=value['value'],
                                       description=value.get('description'))
                      for value in value_list]
            if not values:
                values = None
            enum = ClassesEnum(name=classes_enum['name'],
                               is_bitfield=classes_enum['is_bitfield'],
                               values=values,
                               description=classes_enum.get('description'))
            classes_enums.append(enum)
        if not classes_enums:
            classes_enums = None
        classes_constants = []
        constant_list = classes_single.get('constants', [])
        classes_constants = [ClassesConstant(name=constant['name'],
                                             value=constant['value'],
                                             description=constant.get('description'))
                             for constant in constant_list]
        if not classes_constants:
            classes_constants = None
        classes_methods = []
        for classes_method in classes_single.get('methods', []):
            return_values = classes_method.get('return_value', [])
            return_value = None
            if return_values:
                return_value = ClassesMethodReturnValue(type=return_values.get('type'),
                                                        meta=return_values.get('meta'))
            arg_list = classes_method.get('arguments', [])
            arguments = [ClassesMethodArgument(name=arg['name'],
                                              type=arg['type'],
                                              meta=arg.get('meta'),
                                              default_value=arg.get('default_value'))
                        for arg in arg_list]
            if not arguments:
                arguments = None
            if 'is_required' in classes_method:
                method = ClassesMethodVirtual(name=classes_method['name'],
                                    is_const=classes_method['is_const'],
                                    is_vararg=classes_method['is_vararg'],
                                    is_static=classes_method['is_static'],
                                    is_virtual=classes_method['is_virtual'],
                                    is_required=classes_method.get('is_required'),
                                    hash=classes_method['hash'],
                                    hash_compatibility=classes_method.get('hash_compatibility'),
                                    arguments=arguments,
                                    return_value=return_value,
                                    description=classes_method.get('description'))
            else:
                method = ClassesMethod(name=classes_method['name'],
                                    is_const=classes_method['is_const'],
                                    is_vararg=classes_method['is_vararg'],
                                    is_static=classes_method['is_static'],
                                    is_virtual=classes_method['is_virtual'],
                                    hash=classes_method['hash'],
                                    hash_compatibility=classes_method.get('hash_compatibility'),
                                    arguments=arguments,
                                    return_value=return_value,
                                    description=classes_method.get('description'))
            classes_methods.append(method)
        if not classes_methods:
            classes_methods = None
        classes_signals = []
        for classes_signal in classes_single.get('signals', []):
            arg_list = classes_signal.get('arguments', [])
            arguments = [ClassesSignalArgument(name=arg['name'],
                                               type=arg['type'],
                                               meta=arg.get('meta'))
                         for arg in arg_list]
            if not arguments:
                arguments = None
            signal = ClassesSignal(name=classes_signal['name'],
                                   arguments=arguments,
                                   description=classes_signal.get('description'))
            classes_signals.append(signal)
        if not classes_signals:
            classes_signals = None
        classes_properties = [ClassesProperty(type=arg['type'],
                                              name=arg['name'],
                                              setter=arg.get('setter'),
                                              getter=arg.get('getter'),
                                              index=arg.get('index'),
                                              description=arg.get('description'))
                              for arg in classes_single.get('properties', [])]
        if not classes_properties:
            classes_properties = None
        classes.append(ClassesSingle(name=classes_single['name'],
                                     is_refcounted=classes_single['is_refcounted'],
                                     is_instantiable=classes_single['is_instantiable'],
                                     inherits=classes_single.get('inherits'),
                                     api_type=classes_single['api_type'],
                                     enums=classes_enums,
                                     constants=classes_constants,
                                     methods=classes_methods,
                                     signals=classes_signals,
                                     properties=classes_properties,
                                     brief_description=classes_single.get('brief_description'),
                                     description=classes_single.get('description')))
    return Classes(classes=classes)
            
def parse_singletons(json_data: dict) -> Singletons:
    singletons = []
    for singleton in json_data.get('singletons', []):
        singletons.append(Singleton(name=singleton['name'],
                                    type=singleton['type']))
    return Singletons(singletons=singletons)

def parse_native_structures(json_data: dict) -> NativeStructures:
    native_structures = []
    for native_structure in json_data.get('native_structures', []):
        native_structures.append(NativeStructure(name=native_structure['name'],
                                                format=native_structure['format']))
    return NativeStructures(native_structures=native_structures)

def load_extension_api(path: str) -> GodotInOne:
    with open(path, 'r', encoding='utf-8') as fp:
        json_data = json.load(fp)
    result_header = Header(json_data['header'].get('version_major'),
                    json_data['header'].get('version_minor'),
                    json_data['header'].get('version_patch'),
                    json_data['header'].get('version_status'),
                    json_data['header'].get('version_build'),
                    json_data['header'].get('version_full_name'),
                    json_data['header'].get('precision'))
    result_builtin_class_sizes = parse_builtin_class_sizes(json_data)
    result_builtin_class_member_offsets = parse_builtin_class_member_offsets(json_data)
    result_global_constants = parse_global_constants(json_data)
    result_global_enums = parse_global_enums(json_data)
    result_utility_functions = parse_utility_functions(json_data)
    result_builtin_classes = parse_builtin_classes(json_data)
    result_classes = parse_classes(json_data)
    result_singletons = parse_singletons(json_data)
    result_native_structures = parse_native_structures(json_data)
    all_in_one = GodotInOne(header=result_header,
                            builtin_class_sizes=result_builtin_class_sizes.builtin_class_sizes,
                            builtin_class_member_offsets=result_builtin_class_member_offsets.builtin_class_member_offsets,
                            global_constants=result_global_constants.global_constants,
                            global_enums=result_global_enums.global_enums,
                            utility_functions=result_utility_functions.utility_functions,
                            builtin_classes=result_builtin_classes.builtin_classes,
                            classes=result_classes.classes,
                            singletons=result_singletons.singletons,
                            native_structures=result_native_structures.native_structures)
    return all_in_one