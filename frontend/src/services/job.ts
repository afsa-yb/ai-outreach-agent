import api from "@/lib/api";
import { JobData } from "@/types";

export async function analyzeJob(
  jobDescription: string
): Promise<JobData> {

  const response = await api.post(
    "/job/analyze",
    {
      job_description: jobDescription,
    }
  );

  return response.data;
}