"""
Pydantic models for structured resume data.
"""

from typing import List, Union

from pydantic import BaseModel, Field, field_validator


class EducationData(BaseModel):
    degree: str = ""
    institution: str = ""
    year: str = ""

    @classmethod
    def from_string(cls, value: str):
        return cls(degree=value)


class ProjectData(BaseModel):
    name: str = ""
    description: str = ""

    @classmethod
    def from_string(cls, value: str):
        return cls(name=value)


class ExperienceData(BaseModel):
    title: str = ""
    company: str = ""
    description: str = ""

    @classmethod
    def from_string(cls, value: str):
        return cls(title=value)


class ResumeData(BaseModel):
    """Structured information extracted from a resume."""

    name: str = ""
    email: str = ""
    phone: str = ""

    education: List[EducationData] = Field(
        default_factory=list
    )

    skills: List[str] = Field(
        default_factory=list
    )

    projects: List[ProjectData] = Field(
        default_factory=list
    )

    experience: List[ExperienceData] = Field(
        default_factory=list
    )

    certifications: List[str] = Field(
        default_factory=list
    )

    achievements: List[str] = Field(
        default_factory=list
    )

    summary: str = ""

    @field_validator("education", mode="before")
    @classmethod
    def normalize_education(cls, value):
        if not value:
            return []

        return [
            EducationData.from_string(item)
            if isinstance(item, str)
            else item
            for item in value
        ]

    @field_validator("projects", mode="before")
    @classmethod
    def normalize_projects(cls, value):
        if not value:
            return []

        return [
            ProjectData.from_string(item)
            if isinstance(item, str)
            else item
            for item in value
        ]

    @field_validator("experience", mode="before")
    @classmethod
    def normalize_experience(cls, value):
        if not value:
            return []

        return [
            ExperienceData.from_string(item)
            if isinstance(item, str)
            else item
            for item in value
        ]