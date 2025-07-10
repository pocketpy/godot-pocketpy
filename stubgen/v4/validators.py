import re
from typing import Any

from .schema_py import (
    PyType, PyTypeExpr, PyValueExpr, 
    PyArgument, PyMethod, PyMember, 
    SpecifiedPyMember, PyClass, PyFile
)
from ..tools import ValidatorResults


class ModelValidator:
    """
    用于验证数据模型是否合法的工具类
    """
    
    @staticmethod
    def validate_type(pytype: PyType) -> bool:
        """验证PyType是否合法"""
        results = ValidatorResults()
        results.append(bool(re.fullmatch(r'[A-Za-z0-9_]+', pytype.name)))
        return results.result()
    
    @staticmethod
    def validate_type_expr(expr: PyTypeExpr) -> bool:
        """验证PyTypeExpr是否合法"""
        results = ValidatorResults()
        # TODO: 完善验证逻辑
        return results.result()
    
    @staticmethod
    def validate_value_expr(value: PyValueExpr) -> bool:
        """验证PyValueExpr是否合法"""
        results = ValidatorResults()
        if value.type_expr:
            results.append(ModelValidator.validate_type_expr(value.type_expr))
        return results.result()
    
    @staticmethod
    def validate_argument(argument: PyArgument) -> bool:
        """验证PyArgument是否合法"""
        results = ValidatorResults()
        if argument.type_expr:
            results.append(ModelValidator.validate_type_expr(argument.type_expr))
        else:
            results.append(False)
            
        if argument.default_value:
            results.append(ModelValidator.validate_value_expr(argument.default_value))
            results.append(argument.type_expr == argument.default_value.type_expr)
            
        if argument.name:
            results.append(bool(re.fullmatch(r'[A-Za-z0-9]+', argument.name)))
        else:
            results.append(False)
        return results.result()
    
    @staticmethod
    def validate_method(method: PyMethod) -> bool:
        """验证PyMethod是否合法"""
        results = ValidatorResults()
        if method.return_type_expr:
            results.append(ModelValidator.validate_type_expr(method.return_type_expr))
        else:
            results.append(False)
            
        for argument in method.arguments:
            results.append(ModelValidator.validate_argument(argument))
            
        return results.result()
    
    @staticmethod
    def validate_member(member: PyMember) -> bool:
        """验证PyMember是否合法"""
        results = ValidatorResults()
        
        if member.type_expr:
            results.append(ModelValidator.validate_type_expr(member.type_expr))
        else:
            results.append(False)
        
        if member.value_expr:
            results.append(ModelValidator.validate_value_expr(member.value_expr))
            results.append(member.type_expr == member.value_expr.type_expr)
        
        if member.name:
            results.append(bool(re.fullmatch(r'[A-Za-z0-9]+', member.name)))
        else:
            results.append(False)
            
        return results.result()
    
    @staticmethod
    def validate_specified_member(specified_py_member: SpecifiedPyMember) -> bool:
        """验证SpecifiedPyMember是否合法"""
        return True
    
    @staticmethod
    def validate_class(pyclass: PyClass) -> bool:
        """验证PyClass是否合法"""
        results = ValidatorResults()
        results.append(ModelValidator.validate_type(pyclass.type))
        for member in pyclass.members:
            results.append(ModelValidator.validate_member(member))
        for class_attribute in pyclass.class_attributes:
            results.append(ModelValidator.validate_member(class_attribute))
        for method in pyclass.methods:
            results.append(ModelValidator.validate_method(method))
        return results.result()
    
    @staticmethod
    def validate_file(pyfile: PyFile) -> bool:
        """验证PyFile是否合法"""
        results = ValidatorResults()
        for variable in pyfile.global_variables:
            if isinstance(variable, PyMember):
                results.append(ModelValidator.validate_member(variable))
            else:
                results.append(ModelValidator.validate_specified_member(variable))
        for function in pyfile.global_functions:
            results.append(ModelValidator.validate_method(function))
        for pyclass in pyfile.classes:
            results.append(ModelValidator.validate_class(pyclass))
        return results.result() 