"use client";

import { useState } from "react";

import Navbar from "@/components/layout/navbar";
import Footer from "@/components/layout/footer";

import { uploadResume } from "@/services/resume";
import {
  generateOutreach,
  sendEmail,
} from "@/services/email";

import {
  ResumeData,
  OutreachResponse,
} from "@/types";

export default function Home() {
  const [file, setFile] = useState<File | null>(null);
  const [jobDescription, setJobDescription] = useState("");

  const [resume, setResume] =
    useState<ResumeData | null>(null);

  const [result, setResult] =
    useState<OutreachResponse | null>(null);

  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [recipientEmail, setRecipientEmail] = useState("");
  const [sending, setSending] = useState(false);
  const [sendSuccess, setSendSuccess] = useState("");

  const handleGenerate = async () => {
    if (!file || !jobDescription.trim()) {
      setError("Please upload your resume and enter the job description.");
      return;
    }

    try {
      setLoading(true);
      setError("");
      setResult(null);

      // 1. Analyze resume
      const resumeData = await uploadResume(file);

      setResume(resumeData);

      // 2. Generate complete outreach
      const outreach = await generateOutreach({
        resume: resumeData,
        job_description: jobDescription,
      });

      setResult(outreach);

    } catch (err) {
      console.error(err);
      setError("Failed to generate outreach. Please try again.");
    } finally {
      setLoading(false);
    }
  };
  // Sends the approved email through the connected Gmail account
   const handleSendEmail = async () => {
   try {
    setSending(true);
    setError("");
    setSendSuccess("");

    if (!recipientEmail.trim()) {
      setError("Please enter the recipient email.");
      return;
    }

    if (!result?.email) {
      setError("Please generate an email first.");
      return;
    }

    await sendEmail(
      recipientEmail,
      result.email.subject,
      `${result.email.body}\n\n${result.email.call_to_action}`
    );

    setSendSuccess("Email sent successfully!");

  } catch (err) {
    console.error(err);
    setError("Failed to send email.");
  } finally {
    setSending(false);
  }
};

  return (
    <main className="min-h-screen">

      <Navbar />

      <section>
        <div className="mx-auto max-w-5xl px-6 py-16">

          <div className="text-center">
            <h1 className="text-5xl font-bold">
              AI Outreach Agent
            </h1>

            <p className="mt-4 text-muted-foreground">
              Upload your resume and job description.
              Let AI create your personalized outreach.
            </p>
          </div>

          <div className="mt-12 rounded-xl border p-8">

            <h2 className="text-2xl font-bold">
              Create Your Outreach
            </h2>

            {/* Resume */}
            <div className="mt-6">
              <label className="font-semibold">
                Resume
              </label>

              <input
                type="file"
                accept=".pdf"
                className="mt-2 block w-full rounded-lg border p-3"
                onChange={(e) =>
                  setFile(
                    e.target.files?.[0] || null
                  )
                }
              />

              {file && (
                <p className="mt-2 text-sm text-muted-foreground">
                  {file.name}
                </p>
              )}
            </div>

            {/* Job Description */}
            <div className="mt-6">
              <label className="font-semibold">
                Job Description
              </label>

              <textarea
                className="mt-2 min-h-52 w-full rounded-lg border p-4"
                placeholder="Paste the job description here..."
                value={jobDescription}
                onChange={(e) =>
                  setJobDescription(e.target.value)
                }
              />
            </div>

            {error && (
              <p className="mt-4 text-red-500">
                {error}
              </p>
            )}

            {/* ONE BUTTON */}
            <button
              onClick={handleGenerate}
              disabled={loading}
              className="mt-6 w-full rounded-lg bg-black px-6 py-3 font-semibold text-white disabled:opacity-50"
            >
              {loading
                ? "AI is generating your outreach..."
                : "Generate Personalized Outreach"}
            </button>

          </div>


          {/* AI Personalization */}
          {result?.personalization && (
          <div className="mt-8 rounded-xl border p-8">

          <h2 className="text-2xl font-bold">
           AI Personalization
          </h2>

          <p className="mt-2 text-sm text-muted-foreground">
            How AI decided to position your profile for this opportunity.
          </p>

         <div className="mt-6">
         <h3 className="font-semibold">
          Skills to Highlight
         </h3>

          <div className="mt-2 flex flex-wrap gap-2">
           {result.personalization.highlighted_skills.map(
             (skill, index) => (
              <span
                key={`${skill}-${index}`}
                className="rounded-full border px-3 py-1 text-sm"
             >
               {skill}
             </span>
            )
          )}
         </div>
         </div>

          <div className="mt-6">
          <h3 className="font-semibold">
            Best Project
          </h3>

          <p className="mt-2 text-muted-foreground">
            {result.personalization.best_project}
          </p>
         </div>

          <div className="mt-6">
          <h3 className="font-semibold">
            Job Keywords
          </h3>

          <div className="mt-2 flex flex-wrap gap-2">
           {result.personalization.keywords.map(
           (keyword, index) => (
                <span
                    key={`${keyword}-${index}`}
                   className="rounded-full border px-3 py-1 text-sm"
                 >
                   {keyword}
                </span>
              )
           )}
          </div>
          </div>

          <div className="mt-6">
          <h3 className="font-semibold">
            Company Tone
          </h3>

          <p className="mt-2 text-muted-foreground">
           {result.personalization.company_tone}
          </p>
         </div>

          <div className="mt-6">
          <h3 className="font-semibold">
            Outreach Strategy
          </h3>

          <p className="mt-2 text-muted-foreground">
             {result.personalization.email_strategy}
          </p>
         </div>
         
         <div className="mt-6">
         <h3 className="font-semibold">
           Why These Choices?
         </h3>

         <p className="mt-2 text-muted-foreground">
           {result.personalization.reasoning}
         </p>
         </div>
          </div>
          )}

          {/* Generated Email */}
          {result?.email && (
          <div className="mt-8 rounded-xl border p-8">

          <h2 className="text-2xl font-bold">
           Generated Outreach Email
          </h2>

          <h3 className="mt-6 font-semibold">
           {result.email.subject}
          </h3>

          <p className="mt-4 whitespace-pre-wrap">
           {result.email.body}
          </p>

          <p className="mt-6 font-medium text-muted-foreground">
           {result.email.call_to_action}
          </p>

          {/* Approve & Send */}
         <div className="mt-8 border-t pt-6">

          <h3 className="font-semibold">
            Send Outreach
          </h3>

          <input
           type="email"
           value={recipientEmail}
           onChange={(e) => setRecipientEmail(e.target.value)}
           placeholder="recruiter@company.com"
           className="mt-4 w-full rounded-lg border px-4 py-3"
          />

          <button
          type="button"
          onClick={handleSendEmail}
          disabled={sending}
          className="mt-4 w-full rounded-lg bg-black px-6 py-3 font-semibold text-white disabled:opacity-50"
          >
          {sending ? "Sending..." : "Approve & Send"}
         </button>
          
          {sendSuccess && (
         <p className="mt-4 text-green-600">
           {sendSuccess}
         </p>
         )}
         </div>

          </div>
        )}

        </div>
      </section>

      <Footer />

    </main>
  );
}


