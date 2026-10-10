import api from "@/lib/api";
import { ResumeData } from "@/types";

export async function uploadResume(
  file: File
): Promise<ResumeData> {

  const formData = new FormData();

  formData.append(
    "file",
    file
  );

  const response = await api.post(
    "/resume/upload",
    formData,
    {
      headers: {
        "Content-Type": "multipart/form-data",
      },
    }
  );

  return response.data;
}