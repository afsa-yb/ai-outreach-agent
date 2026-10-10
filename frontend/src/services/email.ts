import api from "@/lib/api";

import {
  OutreachRequest,
  OutreachResponse,
} from "@/types";


export async function generateOutreach(
  payload: OutreachRequest
): Promise<OutreachResponse> {

  const response = await api.post(
    "/outreach/generate",
    payload
  );

  return response.data;
}


export async function sendEmail(
  to: string,
  subject: string,
  body: string
) {

  const response = await api.post(
    "/gmail/send",
    {
      to,
      subject,
      body,
    }
  );

  return response.data;
}