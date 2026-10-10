export default function Navbar() {
  return (
    <header className="border-b bg-background">
      <div className="mx-auto flex h-16 max-w-7xl items-center justify-between px-6">
        <div>
          <h1 className="text-xl font-bold">AI Outreach Agent</h1>
          <p className="text-sm text-muted-foreground">
            Intelligent outreach for jobs, internships and research.
          </p>
        </div>
      </div>
    </header>
  );
}