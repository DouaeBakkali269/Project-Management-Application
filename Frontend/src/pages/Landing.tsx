import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";
import { Navbar } from "@/components/ui/navbar";
import { KanbanSquare, Users, BarChart3, Zap, CheckCircle, Clock, Target } from "lucide-react";
import { Link } from "react-router-dom";

const Landing = () => {
  const features = [
    {
      icon: KanbanSquare,
      title: "Kanban Boards",
      description: "Visualize your workflow with customizable boards, lists, and cards"
    },
    {
      icon: Users,
      title: "Team Collaboration",
      description: "Invite team members, assign tasks, and work together seamlessly"
    },
    {
      icon: BarChart3,
      title: "Progress Tracking",
      description: "Monitor project progress with detailed analytics and reports"
    },
    {
      icon: Zap,
      title: "Real-time Updates",
      description: "See changes instantly as your team updates tasks and projects"
    }
  ];

  const benefits = [
    "Streamline project workflows",
    "Improve team communication", 
    "Track progress in real-time",
    "Customize to fit your needs"
  ];

  return (
    <div className="min-h-screen bg-background">
      <Navbar />
      
      {/* Hero Section */}
      <section className="relative py-section overflow-hidden">
        <div className="absolute inset-0 bg-gradient-hero opacity-5"></div>
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative">
          <div className="text-center">
            <h1 className="text-4xl md:text-6xl font-bold text-foreground mb-6">
              Manage Projects
              <span className="block bg-gradient-hero bg-clip-text text-transparent">
                Like a Pro
              </span>
            </h1>
            <p className="text-xl text-muted-foreground mb-8 max-w-3xl mx-auto">
              TaskFlow helps teams organize, track, and deliver projects with powerful 
              Kanban boards, real-time collaboration, and insightful analytics.
            </p>
            <div className="flex flex-col sm:flex-row gap-4 justify-center">
              <Button size="lg" variant="hero" asChild>
                <Link to="/register">Start Free Trial</Link>
              </Button>
              <Button size="lg" variant="outline" asChild>
                <Link to="/login">Sign In</Link>
              </Button>
            </div>
          </div>
        </div>
      </section>

      {/* Features Section */}
      <section className="py-section bg-muted/30">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-16">
            <h2 className="text-3xl md:text-4xl font-bold text-foreground mb-4">
              Everything you need to succeed
            </h2>
            <p className="text-lg text-muted-foreground max-w-2xl mx-auto">
              Powerful features that help teams stay organized and productive
            </p>
          </div>
          
          <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-8">
            {features.map((feature, index) => (
              <Card key={index} className="text-center hover:shadow-lg transition-all duration-300 border-0 bg-gradient-card">
                <CardContent className="p-6">
                  <div className="w-12 h-12 bg-gradient-primary rounded-lg flex items-center justify-center mx-auto mb-4">
                    <feature.icon className="w-6 h-6 text-white" />
                  </div>
                  <h3 className="text-lg font-semibold text-foreground mb-2">
                    {feature.title}
                  </h3>
                  <p className="text-muted-foreground">
                    {feature.description}
                  </p>
                </CardContent>
              </Card>
            ))}
          </div>
        </div>
      </section>

      {/* Benefits Section */}
      <section className="py-section">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="grid lg:grid-cols-2 gap-12 items-center">
            <div>
              <h2 className="text-3xl md:text-4xl font-bold text-foreground mb-6">
                Why teams choose TaskFlow
              </h2>
              <div className="space-y-4">
                {benefits.map((benefit, index) => (
                  <div key={index} className="flex items-center space-x-3">
                    <CheckCircle className="w-5 h-5 text-success flex-shrink-0" />
                    <span className="text-lg text-foreground">{benefit}</span>
                  </div>
                ))}
              </div>
              <Button size="lg" variant="hero" className="mt-8" asChild>
                <Link to="/register">Get Started Today</Link>
              </Button>
            </div>
            
            <div className="grid grid-cols-2 gap-4">
              <Card className="p-6 text-center bg-gradient-card border-0">
                <Clock className="w-8 h-8 text-primary mx-auto mb-3" />
                <div className="text-2xl font-bold text-foreground">50%</div>
                <div className="text-sm text-muted-foreground">Faster delivery</div>
              </Card>
              <Card className="p-6 text-center bg-gradient-card border-0">
                <Target className="w-8 h-8 text-success mx-auto mb-3" />
                <div className="text-2xl font-bold text-foreground">95%</div>
                <div className="text-sm text-muted-foreground">Project success</div>
              </Card>
              <Card className="p-6 text-center bg-gradient-card border-0">
                <Users className="w-8 h-8 text-secondary mx-auto mb-3" />
                <div className="text-2xl font-bold text-foreground">10k+</div>
                <div className="text-sm text-muted-foreground">Active teams</div>
              </Card>
              <Card className="p-6 text-center bg-gradient-card border-0">
                <BarChart3 className="w-8 h-8 text-warning mx-auto mb-3" />
                <div className="text-2xl font-bold text-foreground">24/7</div>
                <div className="text-sm text-muted-foreground">Insights</div>
              </Card>
            </div>
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="py-section bg-gradient-hero">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
          <h2 className="text-3xl md:text-4xl font-bold text-white mb-4">
            Ready to transform your workflow?
          </h2>
          <p className="text-xl text-white/90 mb-8 max-w-2xl mx-auto">
            Join thousands of teams already using TaskFlow to deliver better projects faster.
          </p>
          <Button size="lg" variant="secondary" asChild>
            <Link to="/register">Start Your Free Trial</Link>
          </Button>
        </div>
      </section>
    </div>
  );
};

export default Landing;