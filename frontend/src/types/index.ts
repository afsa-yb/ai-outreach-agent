export interface EducationData {
  degree: string;
  institution: string;
  year: string;
}

export interface ProjectData {
  name: string;
  description: string;
}

export interface ExperienceData {
  title: string;
  company: string;
  description: string;
}

export interface ResumeData {
  name: string;
  email: string;
  phone: string;

  education: EducationData[];
  skills: string[];
  projects: ProjectData[];
  experience: ExperienceData[];
  certifications: string[];
  achievements: string[];

  summary: string;
}

export interface JobData {
  job_title: string;
  company: string;

  required_skills: string[];
  preferred_skills: string[];
  responsibilities: string[];
  qualifications: string[];
  keywords: string[];

  tone: string;
  summary: string;
}

export interface PersonalizationData {
  highlighted_skills: string[];
  best_project: string;
  keywords: string[];
  company_tone: string;
  email_strategy: string;
  reasoning: string;
}

export interface EmailData {
  subject: string;
  body: string;
  call_to_action: string;
}

export interface OutreachRequest {
  resume: ResumeData;
  job_description: string;
}

export interface OutreachResponse {
  resume: ResumeData;
  job: JobData;
  personalization: PersonalizationData;
  email: EmailData;
}