import React, { useState, useEffect } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { 
  Zap, 
  Code2, 
  Terminal, 
  Cpu, 
  Lightbulb, 
  Palette, 
  Target, 
  Download, 
  Menu, 
  X, 
  Github, 
  Mail, 
  Phone,
  Users,
  Book,
  Globe,
  ChevronRight,
  ArrowRight,
  CheckCircle2,
  Play
} from 'lucide-react';

// --- Components ---

/**
 * Legal Modal Component
 * Displays Privacy Policy and Terms of Service in a centered overlay.
 */
interface LegalModalProps {
  title: string;
  content: React.ReactNode;
  onClose: () => void;
}

const LegalModal = ({ title, content, onClose }: LegalModalProps) => {
  return (
    <div className="fixed inset-0 z-[100] flex items-center justify-center p-4">
      <motion.div 
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        exit={{ opacity: 0 }}
        className="absolute inset-0 bg-black/80 backdrop-blur-sm"
        onClick={onClose}
      />
      <motion.div 
        initial={{ opacity: 0, scale: 0.95, y: 20 }}
        animate={{ opacity: 1, scale: 1, y: 0 }}
        exit={{ opacity: 0, scale: 0.95, y: 20 }}
        className="relative bg-[#0d1117] border border-white/10 rounded-xl p-6 md:p-8 max-w-2xl w-full max-h-[85vh] overflow-y-auto shadow-2xl z-10"
      >
        <button 
          onClick={onClose} 
          className="absolute top-4 right-4 p-2 text-gray-400 hover:text-white hover:bg-white/10 rounded-full transition-colors"
        >
          <X className="w-5 h-5" />
        </button>
        <h2 className="text-2xl font-bold mb-6 text-beacon-cyan">{title}</h2>
        <div className="prose prose-invert prose-sm md:prose-base text-gray-300 space-y-4">
          {content}
        </div>
      </motion.div>
    </div>
  );
};

/**
 * Navigation Bar
 * Professional sticky header with full menu.
 */
const Navbar = () => {
  const [isOpen, setIsOpen] = useState(false);
  const [scrolled, setScrolled] = useState(false);

  useEffect(() => {
    const handleScroll = () => setScrolled(window.scrollY > 20);
    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  const navLinks = [
    { name: 'Features', href: '#features' },
    { name: 'Documentation', href: '#docs' },
    { name: 'Installation', href: '#install' },
    { name: 'Community', href: '#community' },
  ];

  return (
    <nav className={`fixed top-0 w-full z-50 transition-all duration-300 ${scrolled ? 'bg-[#0d1117]/90 backdrop-blur-md border-b border-white/10' : 'bg-transparent'}`}>
      <div className="max-w-7xl mx-auto px-6">
        <div className="flex items-center justify-between h-20">
          {/* Logo */}
          <a href="https://github.com/ADIVIDAN1012/Beacon-Labs" className="flex items-center gap-3 group">
            <div className="relative">
              <div className="absolute inset-0 bg-beacon-cyan blur-lg opacity-20 group-hover:opacity-40 transition-opacity" />
              <img src="/logo.png" alt="Beacon Logo" className="w-8 h-8 relative z-10" />
            </div>
            <span className="text-xl font-bold tracking-tight text-white">Beacon</span>
          </a>

          {/* Desktop Nav */}
          <div className="hidden md:flex items-center gap-8">
            {navLinks.map((link) => (
              <a 
                key={link.name} 
                href={link.href} 
                className="text-gray-300 hover:text-beacon-cyan transition-colors font-medium text-sm tracking-wide"
              >
                {link.name}
              </a>
            ))}
            <a 
              href="https://github.com/ADIVIDAN1012/Beacon-Labs/releases/download/v1.0.0/BPL.exe"
              className="flex items-center gap-2 px-4 py-2 bg-white/10 border border-white/10 text-white font-medium rounded-lg hover:bg-beacon-cyan hover:text-beacon-darker hover:border-beacon-cyan transition-all text-sm"
            >
              <Download className="w-4 h-4" />
              Download v1.0.0
            </a>
          </div>

          {/* Mobile Menu Button */}
          <button onClick={() => setIsOpen(!isOpen)} className="md:hidden text-white p-2">
            {isOpen ? <X /> : <Menu />}
          </button>
        </div>
      </div>

      {/* Mobile Menu */}
      <AnimatePresence>
        {isOpen && (
          <motion.div 
            initial={{ opacity: 0, height: 0 }}
            animate={{ opacity: 1, height: 'auto' }}
            exit={{ opacity: 0, height: 0 }}
            className="md:hidden bg-[#0d1117] border-b border-white/10 overflow-hidden"
          >
            <div className="px-6 py-4 flex flex-col gap-4">
              {navLinks.map((link) => (
                <a 
                  key={link.name} 
                  href={link.href} 
                  onClick={() => setIsOpen(false)}
                  className="text-gray-300 hover:text-beacon-cyan py-2 block border-b border-white/5"
                >
                  {link.name}
                </a>
              ))}
              <a 
                href="https://github.com/ADIVIDAN1012/Beacon-Labs/releases/download/v1.0.0/BPL.exe"
                className="text-beacon-cyan font-bold py-3 block flex items-center gap-2"
              >
                <Download className="w-4 h-4" /> Download BPL
              </a>
            </div>
          </motion.div>
        )}
      </AnimatePresence>
    </nav>
  );
};

/**
 * Interactive Code Window
 * Tabs for different code examples.
 */
const CodeWindow = () => {
  const [activeTab, setActiveTab] = useState<'hello' | 'variables' | 'logic'>('hello');

  const tabs = [
    { id: 'hello', label: 'hello.bpl' },
    { id: 'variables', label: 'variables.bpl' },
    { id: 'logic', label: 'logic.bpl' },
  ];

  const snippets = {
    hello: (
      <>
        <span className="text-gray-500 italic">{"< String Interpolation >"}</span><br/>
        <span className="text-beacon-purple font-bold">spec</span> <span className="text-white">main</span><span className="text-gray-400">()</span> <span className="text-yellow-400">{"{"}</span><br/>
        <span className="pl-4 inline-block text-beacon-purple font-bold">show</span><span className="text-gray-400">(</span><span className="text-green-400">"Enter a number:"</span><span className="text-gray-400">)</span><br/>
        <span className="pl-4 inline-block text-beacon-purple font-bold">firm</span> <span className="text-white">x</span> <span className="text-beacon-cyan">=</span> <span className="text-beacon-purple font-bold">ask</span><span className="text-gray-400">(</span><span className="text-green-400">""</span><span className="text-gray-400">)</span><br/>
        <span className="pl-4 inline-block text-beacon-purple font-bold">show</span><span className="text-gray-400">(</span><span className="text-green-400">"You entered: |x|"</span><span className="text-gray-400">)</span><br/>
        <span className="text-yellow-400">{"}"}</span><br/>
        <span className="text-beacon-purple font-bold">funcall</span> <span className="text-white">main</span><span className="text-gray-400">()</span>
      </>
    ),
    variables: (
      <>
        <span className="text-gray-500 italic">{"< Constants & Types >"}</span><br/>
        <span className="text-beacon-purple font-bold">firm</span> <span className="text-white">PI</span> <span className="text-beacon-cyan">=</span> <span className="text-beacon-cyan">3.14159</span><br/>
        <span className="text-beacon-purple font-bold">firm</span> <span className="text-white">isActive</span> <span className="text-beacon-cyan">=</span> <span className="text-beacon-purple">On</span><br/>
        <span className="text-beacon-purple font-bold">firm</span> <span className="text-white">nothing</span> <span className="text-beacon-cyan">=</span> <span className="text-beacon-purple">Nil</span><br/>
        <span className="text-gray-500 italic">{"< PI = 3.14 -> Runtime Error! >"}</span><br/>
        <span className="text-beacon-purple font-bold">show</span><span className="text-gray-400">(</span><span className="text-green-400">"Status: |isActive|"</span><span className="text-gray-400">)</span>
      </>
    ),
    logic: (
      <>
        <span className="text-gray-500 italic">{"< Readable Control Flow >"}</span><br/>
        <span className="text-beacon-purple font-bold">spec</span> <span className="text-white">check_score</span><span className="text-gray-400">(</span><span className="text-white">score</span><span className="text-gray-400">)</span> <span className="text-yellow-400">{"{"}</span><br/>
        <span className="pl-4 inline-block text-beacon-purple font-bold">check</span> <span className="text-white">score</span> <span className="text-beacon-cyan">{">"}</span> <span className="text-beacon-cyan">90</span> <span className="text-yellow-400">{"{"}</span><br/>
        <span className="pl-8 inline-block text-beacon-purple font-bold">forward</span> <span className="text-green-400">"Excellent!"</span><br/>
        <span className="pl-4 inline-block text-yellow-400">{"}"}</span> <span className="text-beacon-purple font-bold">alter</span> <span className="text-white">score</span> <span className="text-beacon-cyan">{">"}</span> <span className="text-beacon-cyan">60</span> <span className="text-yellow-400">{"{"}</span><br/>
        <span className="pl-8 inline-block text-beacon-purple font-bold">forward</span> <span className="text-green-400">"Good job!"</span><br/>
        <span className="pl-4 inline-block text-yellow-400">{"}"}</span> <span className="text-beacon-purple font-bold">altern</span> <span className="text-yellow-400">{"{"}</span><br/>
        <span className="pl-8 inline-block text-beacon-purple font-bold">forward</span> <span className="text-green-400">"Keep trying!"</span><br/>
        <span className="pl-4 inline-block text-yellow-400">{"}"}</span><br/>
        <span className="text-yellow-400">{"}"}</span>
      </>
    )
  };

  return (
    <div className="relative rounded-xl overflow-hidden bg-[#0d1117] border border-white/10 shadow-2xl shadow-beacon-purple/10">
      {/* Window Header */}
      <div className="flex items-center justify-between px-4 py-3 bg-white/5 border-b border-white/5">
        <div className="flex gap-2">
          <div className="w-3 h-3 rounded-full bg-red-500/80" />
          <div className="w-3 h-3 rounded-full bg-yellow-500/80" />
          <div className="w-3 h-3 rounded-full bg-green-500/80" />
        </div>
        <div className="flex gap-1 bg-black/20 rounded-lg p-1">
          {tabs.map(tab => (
            <button
              key={tab.id}
              onClick={() => setActiveTab(tab.id as any)}
              className={`px-3 py-1 text-xs font-mono rounded-md transition-all ${
                activeTab === tab.id 
                  ? 'bg-beacon-purple/20 text-beacon-cyan shadow-sm' 
                  : 'text-gray-500 hover:text-gray-300'
              }`}
            >
              {tab.label}
            </button>
          ))}
        </div>
      </div>
      {/* Window Body */}
      <div className="p-6 md:p-8 overflow-x-auto min-h-[200px] flex items-center">
        <div className="font-mono text-sm sm:text-base leading-loose whitespace-nowrap">
          {snippets[activeTab]}
        </div>
      </div>
    </div>
  );
};

/**
 * Hero Section
 */
const Hero = () => {
  return (
    <section className="relative pt-32 pb-20 lg:pt-48 lg:pb-32 overflow-hidden">
      {/* Background Gradients */}
      <div className="absolute top-0 left-1/2 -translate-x-1/2 w-[1000px] h-[600px] bg-beacon-purple/10 rounded-full blur-[120px] -z-10" />
      <div className="absolute bottom-0 right-0 w-[600px] h-[600px] bg-beacon-cyan/5 rounded-full blur-[120px] -z-10" />

      <div className="max-w-7xl mx-auto px-6 grid lg:grid-cols-2 gap-16 items-center">
        {/* Left: Content */}
        <motion.div 
          initial={{ opacity: 0, x: -30 }}
          animate={{ opacity: 1, x: 0 }}
          transition={{ duration: 0.8, ease: "easeOut" }}
          className="space-y-8"
        >
          <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-beacon-cyan/10 border border-beacon-cyan/20 text-beacon-cyan text-xs font-bold uppercase tracking-wider">
            Latest Release: v1.0.0
          </div>

          <h1 className="text-5xl lg:text-7xl font-bold leading-tight">
            Illuminate Your <br />
            <span className="text-transparent bg-clip-text bg-gradient-to-r from-beacon-cyan to-beacon-purple">Logic</span>
          </h1>

          <p className="text-xl text-gray-400 leading-relaxed max-w-lg">
            A statically-typed, readable programming language designed for both rapid scripting and high-performance system applications.
          </p>

          <div className="flex flex-col sm:flex-row gap-4 pt-4">
            <a 
              href="https://github.com/ADIVIDAN1012/Beacon-Labs/releases/download/v1.0.0/BPL.exe"
              className="group flex items-center justify-center gap-3 px-8 py-4 bg-beacon-cyan text-beacon-darker font-bold rounded-lg hover:bg-white transition-all transform hover:scale-[1.02] shadow-[0_0_20px_rgba(0,255,255,0.3)]"
            >
              <Download className="w-5 h-5" />
              Download for Windows
            </a>
            <a 
              href="#docs"
              className="flex items-center justify-center gap-3 px-8 py-4 bg-white/5 border border-white/10 text-white font-semibold rounded-lg hover:bg-white/10 hover:border-beacon-purple/50 transition-all"
            >
              <Book className="w-5 h-5 text-beacon-purple" />
              Read Documentation
            </a>
          </div>
          <div className="flex items-center gap-4 text-sm text-gray-500">
            <span className="flex items-center gap-1"><CheckCircle2 className="w-4 h-4 text-green-500" /> Open Source</span>
            <span className="flex items-center gap-1"><CheckCircle2 className="w-4 h-4 text-green-500" /> MIT License</span>
            <span className="flex items-center gap-1"><CheckCircle2 className="w-4 h-4 text-green-500" /> v1.0.0 Stable</span>
          </div>
        </motion.div>

        {/* Right: Code Window */}
        <motion.div 
          initial={{ opacity: 0, y: 30 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8, delay: 0.2, ease: "easeOut" }}
          className="relative"
        >
          <CodeWindow />
          
          {/* Decorative Elements */}
          <div className="absolute -bottom-10 -right-10 w-32 h-32 bg-beacon-purple rounded-full blur-[60px] opacity-20 -z-10" />
          <div className="absolute -top-10 -left-10 w-32 h-32 bg-beacon-cyan rounded-full blur-[60px] opacity-20 -z-10" />
        </motion.div>
      </div>
    </section>
  );
};

/**
 * Feature Grid
 */
const Features = () => {
  const features = [
    {
      icon: <Lightbulb className="w-6 h-6" />,
      title: "Readable Syntax",
      desc: "English-like keywords make logic instantly understandable, reducing cognitive load for new and experienced developers."
    },
    {
      icon: <Cpu className="w-6 h-6" />,
      title: "Native Performance",
      desc: "Transpiles directly to optimized C code, giving you the raw performance of a low-level language with high-level ease."
    },
    {
      icon: <Terminal className="w-6 h-6" />,
      title: "Rapid Prototyping",
      desc: "Built-in interpreter allows for instant feedback loops, perfect for scripts, tools, and learning."
    },
    {
      icon: <Target className="w-6 h-6" />,
      title: "Smart Type Safety",
      desc: "Static typing with intelligent inference. Catches errors at compile time while keeping code verbose-free."
    }
  ];

  return (
    <section id="features" className="py-24 bg-white/[0.02]">
      <div className="max-w-7xl mx-auto px-6">
        <div className="flex flex-col md:flex-row justify-between items-end mb-16 gap-6">
          <div>
            <h2 className="text-3xl md:text-4xl font-bold mb-4">Core Principles</h2>
            <p className="text-gray-400 max-w-xl">
              Beacon is designed to bridge the gap between human readability and machine efficiency.
            </p>
          </div>
          <a href="#docs" className="text-beacon-cyan hover:text-white flex items-center gap-2 transition-colors font-medium">
            Explore all features <ArrowRight className="w-4 h-4" />
          </a>
        </div>

        <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-6">
          {features.map((f, i) => (
            <div key={i} className="p-6 rounded-2xl bg-white/5 border border-white/5 hover:border-beacon-purple/50 transition-colors group">
              <div className="w-12 h-12 rounded-lg bg-beacon-dark border border-white/10 flex items-center justify-center text-beacon-purple mb-4 group-hover:text-beacon-cyan transition-colors">
                {f.icon}
              </div>
              <h3 className="text-lg font-bold mb-2">{f.title}</h3>
              <p className="text-sm text-gray-400 leading-relaxed">{f.desc}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};

/**
 * Quick Documentation Section
 */
const Documentation = () => {
  return (
    <section id="docs" className="py-24 relative overflow-hidden">
      <div className="max-w-7xl mx-auto px-6">
        <div className="grid lg:grid-cols-12 gap-12">
          {/* Docs Content */}
          <div className="lg:col-span-8">
            <h2 className="text-3xl font-bold mb-8">Language Reference</h2>
            
            <div className="space-y-8">
              <div className="bg-[#0d1117] rounded-xl border border-white/10 overflow-hidden">
                <div className="px-6 py-4 border-b border-white/10 bg-white/5 font-bold flex justify-between items-center">
                  <span>Keywords & Syntax</span>
                  <span className="text-xs uppercase text-gray-500 tracking-wider">Cheat Sheet</span>
                </div>
                <div className="p-6 grid gap-6 sm:grid-cols-2">
                  <div>
                    <code className="text-beacon-purple font-bold">firm</code>
                    <p className="text-sm text-gray-400 mt-1">Constant declaration. Cannot be reassigned after initialization.</p>
                  </div>
                  <div>
                    <code className="text-beacon-purple font-bold">spec</code>
                    <p className="text-sm text-gray-400 mt-1">Function declaration. Use <code className="text-xs">forward</code> to return values.</p>
                  </div>
                  <div>
                    <code className="text-beacon-purple font-bold">check/alter/altern</code>
                    <p className="text-sm text-gray-400 mt-1">If/else if/else conditionals. Tested and working.</p>
                  </div>
                  <div>
                    <code className="text-beacon-purple font-bold">traverse</code>
                    <p className="text-sm text-gray-400 mt-1">For-loop over ranges: <code className="text-xs">from X to Y</code></p>
                  </div>
                  <div>
                    <code className="text-beacon-purple font-bold">show/ask</code>
                    <p className="text-sm text-gray-400 mt-1">Output and input. <code className="text-xs">ask()</code> auto-detects types.</p>
                  </div>
                  <div>
                    <code className="text-beacon-purple font-bold">attempt/trap</code>
                    <p className="text-sm text-gray-400 mt-1">Try-catch error handling with <code className="text-xs">conclude</code> (finally).</p>
                  </div>
                </div>
              </div>

              <div className="grid md:grid-cols-2 gap-6">
                 <div className="bg-[#0d1117] rounded-xl border border-white/10 p-6">
                    <h3 className="font-bold text-white mb-4 flex items-center gap-2">
                      <Terminal className="w-4 h-4 text-beacon-cyan" /> CLI Commands
                    </h3>
                    <ul className="space-y-3 font-mono text-sm">
                      <li className="flex gap-4">
                        <span className="text-gray-500">$</span>
                        <span>BPL <span className="text-beacon-purple">run</span> main.bpl</span>
                      </li>
                      <li className="flex gap-4">
                        <span className="text-gray-500">$</span>
                        <span>BPL <span className="text-beacon-purple">compile</span> main.bpl</span>
                      </li>
                      <li className="flex gap-4">
                        <span className="text-gray-500">$</span>
                        <span>BPL <span className="text-beacon-purple">version</span></span>
                      </li>
                    </ul>
                 </div>
                 
                 <div className="bg-gradient-to-br from-beacon-purple/20 to-beacon-dark rounded-xl border border-beacon-purple/20 p-6 relative overflow-hidden">
                    <div className="absolute top-0 right-0 p-4 opacity-20">
                      <Code2 className="w-24 h-24" />
                    </div>
                    <h3 className="font-bold text-white mb-2">VS Code Support</h3>
                    <p className="text-sm text-gray-400 mb-4">
                      Get full syntax highlighting, snippets, and error checking directly in your editor.
                    </p>
                    <a 
                      href="https://github.com/ADIVIDAN1012/Beacon-Labs/releases/download/v1.0.0/beacon-0.0.3.vsix"
                      className="inline-flex items-center gap-2 text-sm font-bold text-beacon-cyan hover:underline"
                    >
                      Install Extension <ChevronRight className="w-4 h-4" />
                    </a>
                 </div>
              </div>
            </div>
          </div>

          {/* Sidebar */}
          <div className="lg:col-span-4 space-y-6">
            <div className="p-6 rounded-2xl bg-white/5 border border-white/10">
              <h3 className="font-bold mb-4">Resources</h3>
              <ul className="space-y-3 text-sm">
                <li><a href="https://github.com/ADIVIDAN1012/Beacon-Labs/tree/main/docs/Lib.md" target="_blank" rel="noreferrer" className="text-gray-400 hover:text-beacon-cyan flex items-center justify-between group">Standard Library <ArrowRight className="w-3 h-3 opacity-0 group-hover:opacity-100 transition-opacity" /></a></li>
                <li><a href="https://github.com/ADIVIDAN1012/Beacon-Labs/tree/main/docs/Syntax.md" target="_blank" rel="noreferrer" className="text-gray-400 hover:text-beacon-cyan flex items-center justify-between group">Language Spec <ArrowRight className="w-3 h-3 opacity-0 group-hover:opacity-100 transition-opacity" /></a></li>
                <li><a href="https://github.com/ADIVIDAN1012/Beacon-Labs/tree/main/examples" target="_blank" rel="noreferrer" className="text-gray-400 hover:text-beacon-cyan flex items-center justify-between group">Examples Repo <ArrowRight className="w-3 h-3 opacity-0 group-hover:opacity-100 transition-opacity" /></a></li>
              </ul>
            </div>
            
            <div className="p-6 rounded-2xl bg-beacon-cyan/5 border border-beacon-cyan/20">
              <h3 className="font-bold mb-2 text-beacon-cyan">Contributions</h3>
              <p className="text-sm text-gray-400 mb-4">
                Beacon is open source. Help us improve the compiler or add new features.
              </p>
              <a 
                href="https://github.com/ADIVIDAN1012/Beacon-Labs" 
                target="_blank"
                rel="noreferrer"
                className="w-full block text-center py-2 bg-beacon-cyan text-beacon-darker font-bold rounded-lg hover:bg-white transition-colors text-sm"
              >
                View on GitHub
              </a>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

/**
 * Footer Section
 */
interface FooterProps {
  onOpenPrivacy: () => void;
  onOpenTerms: () => void;
}

const Footer = ({ onOpenPrivacy, onOpenTerms }: FooterProps) => {
  return (
    <footer id="community" className="bg-[#05090f] pt-20 pb-10 border-t border-white/10 text-sm">
      <div className="max-w-7xl mx-auto px-6">
        <div className="grid md:grid-cols-2 lg:grid-cols-5 gap-10 mb-16">
          
          {/* Brand Column */}
          <div className="lg:col-span-2">
            <div className="flex items-center gap-2 mb-4">
              <img src="/logo.png" alt="Beacon Logo" className="w-7 h-7" />
              <span className="text-xl font-bold text-white">Beacon Labs</span>
            </div>
            <p className="text-gray-500 mb-6 max-w-sm">
              Empowering developers with tools that illuminate logic and simplify complexity. 
              Built for the modern web and systems programming era.
            </p>
            <div className="flex gap-4">
              <a href="https://github.com/ADIVIDAN1012/Beacon-Labs" target="_blank" rel="noreferrer" className="text-gray-400 hover:text-white transition-colors"><Github className="w-5 h-5" /></a>
              <a href="https://wa.me/916005706055" target="_blank" rel="noreferrer" className="text-gray-400 hover:text-white transition-colors"><Phone className="w-5 h-5" /></a>
              <a href="mailto:aadityasadhu50@gmail.com" className="text-gray-400 hover:text-white transition-colors"><Mail className="w-5 h-5" /></a>
            </div>
          </div>

          {/* Links Column 1 */}
          <div>
            <h4 className="font-bold text-white mb-4">Product</h4>
            <ul className="space-y-2">
              <li><a href="https://github.com/ADIVIDAN1012/Beacon-Labs/releases/download/v1.0.0/BPL.exe" className="text-gray-400 hover:text-beacon-cyan transition-colors">Download Compiler</a></li>
              <li><a href="https://github.com/ADIVIDAN1012/Beacon-Labs/releases/download/v1.0.0/beacon-0.0.3.vsix" className="text-gray-400 hover:text-beacon-cyan transition-colors">VS Code Extension</a></li>
              <li><a href="https://github.com/ADIVIDAN1012/Beacon-Labs" className="text-gray-400 hover:text-beacon-cyan transition-colors">Source Code</a></li>
              <li><a href="https://github.com/ADIVIDAN1012/Beacon-Labs/releases" target="_blank" rel="noreferrer" className="text-gray-400 hover:text-beacon-cyan transition-colors">Changelog</a></li>
            </ul>
          </div>

          {/* Links Column 2 */}
          <div>
            <h4 className="font-bold text-white mb-4">Community</h4>
            <ul className="space-y-2">
              <li><a href="https://chat.whatsapp.com/DRWgaZFQUlELZNwqVqLsw1" target="_blank" rel="noreferrer" className="text-gray-400 hover:text-beacon-cyan transition-colors flex items-center gap-2"><Users className="w-3 h-3" /> WhatsApp Group</a></li>
              <li><a href="https://github.com/ADIVIDAN1012/Beacon-Labs/issues" target="_blank" rel="noreferrer" className="text-gray-400 hover:text-beacon-cyan transition-colors">Report Issues</a></li>
              <li><a href="https://github.com/ADIVIDAN1012/Beacon-Labs/discussions" target="_blank" rel="noreferrer" className="text-gray-400 hover:text-beacon-cyan transition-colors">Discussions</a></li>
            </ul>
          </div>

          {/* Links Column 3 */}
          <div>
            <h4 className="font-bold text-white mb-4">Legal</h4>
            <ul className="space-y-2">
              <li><button onClick={onOpenPrivacy} className="text-gray-400 hover:text-beacon-cyan transition-colors text-left">Privacy Policy</button></li>
              <li><button onClick={onOpenTerms} className="text-gray-400 hover:text-beacon-cyan transition-colors text-left">Terms of Service</button></li>
              <li><span className="text-gray-600 cursor-not-allowed">Cookie Policy</span></li>
            </ul>
          </div>
        </div>

        <div className="border-t border-white/5 pt-8 flex flex-col md:flex-row justify-between items-center gap-4 text-gray-600">
          <p>© 2025 Beacon Labs. All rights reserved.</p>
          <div className="flex items-center gap-2 text-xs">
            <span className="w-2 h-2 rounded-full bg-green-500"></span>
            All Systems Operational
          </div>
        </div>
      </div>
    </footer>
  );
};

/**
 * Main App Component
 */
const App = () => {
  const [activeModal, setActiveModal] = useState<'privacy' | 'terms' | null>(null);

  const privacyContent = (
    <>
      <p><strong>Effective Date: January 15, 2025</strong></p>
      <p>
        Beacon Labs ("we", "our", or "us") is committed to protecting your privacy. This Privacy Policy explains how our organization uses the personal data we collect from you when you use our website and software products.
      </p>
      <h3>1. Data We Collect</h3>
      <p>
        Our compiler (BPL.exe) and VS Code extension operate locally on your machine. We do not transmit your source code, environment variables, or compilation artifacts to any external servers.
      </p>
      <h3>2. Analytics</h3>
      <p>
        We may collect anonymous aggregated data regarding website visits and download counts via GitHub API to help us improve the platform. No personally identifiable information (PII) is attached to this data.
      </p>
      <h3>3. Third-Party Links</h3>
      <p>
        Our website contains links to other websites (e.g., GitHub, WhatsApp). Our privacy policy applies only to our website, so if you click on a link to another website, you should read their privacy policy.
      </p>
      <h3>4. Updates</h3>
      <p>
        We keep our privacy policy under regular review and places any updates on this web page.
      </p>
    </>
  );

  const termsContent = (
    <>
      <p><strong>Effective Date: January 15, 2025</strong></p>
      <p>
        Welcome to Beacon Labs. By downloading or using our software, you agree to comply with and be bound by the following terms and conditions of use.
      </p>
      <h3>1. License Grant</h3>
      <p>
        Beacon (BPL) is open-source software distributed under the MIT License. You are granted a perpetual, worldwide, non-exclusive, no-charge, royalty-free, irrevocable copyright license to reproduce, prepare derivative works of, publicly display, publicly perform, sublicense, and distribute the Work and such Derivative Works.
      </p>
      <h3>2. Prohibited Uses</h3>
      <p>
        You may not use the software for any purpose that is unlawful or prohibited by these Terms.
      </p>
      <h3>3. Limitation of Liability</h3>
      <p>
        In no event shall Beacon Labs be liable for any direct, indirect, incidental, special, exemplary, or consequential damages (including, but not limited to, procurement of substitute goods or services; loss of use, data, or profits; or business interruption) however caused.
      </p>
      <h3>4. Modifications</h3>
      <p>
        We reserve the right to revise these terms at any time. By using this website you are agreeing to be bound by the then current version of these Terms of Service.
      </p>
    </>
  );

  return (
    <div className="min-h-screen flex flex-col font-sans selection:bg-beacon-cyan selection:text-beacon-darker">
      <Navbar />
      <main className="flex-grow">
        <Hero />
        <Features />
        <Documentation />
        {/* Installation Section */}
        <section id="install" className="py-24 bg-[#0d1117] border-y border-white/5">
           <div className="max-w-4xl mx-auto px-6 text-center">
             <h2 className="text-3xl font-bold mb-6">Get Started in Seconds</h2>
             <p className="text-gray-400 mb-10">No complex dependencies. Just download the binary and start coding.</p>
             
             <div className="bg-black/40 border border-white/10 rounded-xl p-6 md:p-10 backdrop-blur-sm">
                <div className="flex flex-col md:flex-row items-center justify-between gap-6 mb-8 pb-8 border-b border-white/5">
                   <div className="text-left">
                     <h3 className="text-xl font-bold text-white mb-1">Windows Installer</h3>
                     <p className="text-sm text-gray-500">For Windows 10/11 (x64)</p>
                   </div>
                   <a 
                    href="https://github.com/ADIVIDAN1012/Beacon-Labs/releases/download/v1.0.0/BPL.exe"
                    className="w-full md:w-auto px-6 py-3 bg-beacon-cyan text-beacon-darker font-bold rounded-lg hover:bg-white transition-colors"
                   >
                     Download .exe
                   </a>
                </div>
                
                <div className="text-left font-mono text-sm bg-black/50 p-4 rounded-lg border border-white/5 flex items-center justify-between group">
                  <span className="text-gray-400 select-all">$ BPL version</span>
                  <span className="text-beacon-cyan">Beacon v1.0.0</span>
                </div>
             </div>
             
             <p className="mt-8 text-sm text-gray-500">
               Looking for Linux or macOS? <a href="https://github.com/ADIVIDAN1012/Beacon-Labs" className="text-beacon-cyan hover:underline">Build from source</a>
             </p>
           </div>
        </section>
      </main>
      <Footer 
        onOpenPrivacy={() => setActiveModal('privacy')} 
        onOpenTerms={() => setActiveModal('terms')} 
      />

      <AnimatePresence>
        {activeModal === 'privacy' && (
          <LegalModal 
            key="privacy"
            title="Privacy Policy"
            content={privacyContent}
            onClose={() => setActiveModal(null)}
          />
        )}
        {activeModal === 'terms' && (
          <LegalModal 
            key="terms"
            title="Terms of Service"
            content={termsContent}
            onClose={() => setActiveModal(null)}
          />
        )}
      </AnimatePresence>
    </div>
  );
};

export default App;
