import { Button } from "@/components/ui/button";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Navbar } from "@/components/ui/navbar";
import { Plus, BarChart3, Users, Calendar, TrendingUp, Clock, CheckCircle } from "lucide-react";
import { Link } from "react-router-dom";

const Dashboard = () => {
  const user = {
    name: "John Doe",
    email: "john@example.com",
    avatar: "/placeholder.svg"
  };

  const recentProjects = [
    {
      id: 1,
      name: "Website Redesign",
      description: "Complete overhaul of company website",
      progress: 75,
      dueDate: "2024-02-15",
      status: "In Progress",
      members: 5
    },
    {
      id: 2,
      name: "Mobile App Development",
      description: "iOS and Android app for customer portal",
      progress: 45,
      dueDate: "2024-03-01",
      status: "In Progress",
      members: 3
    },
    {
      id: 3,
      name: "Marketing Campaign",
      description: "Q1 marketing campaign planning and execution",
      progress: 90,
      dueDate: "2024-01-30",
      status: "Review",
      members: 4
    }
  ];

  const stats = [
    {
      title: "Active Projects",
      value: "12",
      change: "+2 from last month",
      icon: BarChart3,
      trend: "up"
    },
    {
      title: "Team Members",
      value: "24",
      change: "+3 this week",
      icon: Users,
      trend: "up"
    },
    {
      title: "Tasks Completed",
      value: "156",
      change: "+12 today",
      icon: CheckCircle,
      trend: "up"
    },
    {
      title: "Average Completion",
      value: "87%",
      change: "+5% improvement",
      icon: TrendingUp,
      trend: "up"
    }
  ];

  return (
    <div className="min-h-screen bg-background">
      <Navbar user={user} />
      
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        {/* Header */}
        <div className="flex justify-between items-center mb-8">
          <div>
            <h1 className="text-3xl font-bold text-foreground">Welcome back, {user.name}</h1>
            <p className="text-muted-foreground mt-1">Here's what's happening with your projects today.</p>
          </div>
          <Button variant="hero" asChild>
            <Link to="/projects/new">
              <Plus className="w-4 h-4 mr-2" />
              New Project
            </Link>
          </Button>
        </div>

        {/* Stats Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
          {stats.map((stat, index) => (
            <Card key={index} className="bg-gradient-card border-0">
              <CardContent className="p-6">
                <div className="flex items-center justify-between">
                  <div>
                    <p className="text-sm font-medium text-muted-foreground">{stat.title}</p>
                    <p className="text-2xl font-bold text-foreground">{stat.value}</p>
                  </div>
                  <div className="w-12 h-12 bg-gradient-primary rounded-lg flex items-center justify-center">
                    <stat.icon className="w-6 h-6 text-white" />
                  </div>
                </div>
                <p className="text-xs text-success mt-2 flex items-center">
                  <TrendingUp className="w-3 h-3 mr-1" />
                  {stat.change}
                </p>
              </CardContent>
            </Card>
          ))}
        </div>

        {/* Recent Projects */}
        <div className="grid lg:grid-cols-3 gap-8">
          <div className="lg:col-span-2">
            <Card className="bg-gradient-card border-0">
              <CardHeader>
                <div className="flex items-center justify-between">
                  <div>
                    <CardTitle>Recent Projects</CardTitle>
                    <CardDescription>Your most active projects</CardDescription>
                  </div>
                  <Button variant="outline" asChild>
                    <Link to="/projects">View All</Link>
                  </Button>
                </div>
              </CardHeader>
              <CardContent>
                <div className="space-y-4">
                  {recentProjects.map((project) => (
                    <div key={project.id} className="flex items-center justify-between p-4 rounded-lg border bg-background/50">
                      <div className="flex-1">
                        <div className="flex items-center justify-between mb-2">
                          <h3 className="font-semibold text-foreground">{project.name}</h3>
                          <span className={`px-2 py-1 rounded-full text-xs font-medium ${
                            project.status === 'In Progress' ? 'bg-primary/10 text-primary' :
                            project.status === 'Review' ? 'bg-warning/10 text-warning' :
                            'bg-success/10 text-success'
                          }`}>
                            {project.status}
                          </span>
                        </div>
                        <p className="text-sm text-muted-foreground mb-3">{project.description}</p>
                        <div className="flex items-center justify-between text-xs text-muted-foreground">
                          <div className="flex items-center space-x-4">
                            <div className="flex items-center">
                              <Users className="w-3 h-3 mr-1" />
                              {project.members} members
                            </div>
                            <div className="flex items-center">
                              <Calendar className="w-3 h-3 mr-1" />
                              Due {project.dueDate}
                            </div>
                          </div>
                          <span className="font-medium">{project.progress}% complete</span>
                        </div>
                        <div className="w-full bg-muted rounded-full h-2 mt-2">
                          <div 
                            className="bg-gradient-primary h-2 rounded-full transition-all duration-300" 
                            style={{ width: `${project.progress}%` }}
                          ></div>
                        </div>
                      </div>
                    </div>
                  ))}
                </div>
              </CardContent>
            </Card>
          </div>

          {/* Quick Actions */}
          <div className="space-y-6">
            <Card className="bg-gradient-card border-0">
              <CardHeader>
                <CardTitle>Quick Actions</CardTitle>
                <CardDescription>Common tasks and shortcuts</CardDescription>
              </CardHeader>
              <CardContent className="space-y-3">
                <Button variant="outline" className="w-full justify-start" asChild>
                  <Link to="/projects/new">
                    <Plus className="w-4 h-4 mr-2" />
                    Create New Project
                  </Link>
                </Button>
                <Button variant="outline" className="w-full justify-start" asChild>
                  <Link to="/projects">
                    <BarChart3 className="w-4 h-4 mr-2" />
                    View All Projects
                  </Link>
                </Button>
                <Button variant="outline" className="w-full justify-start" asChild>
                  <Link to="/profile">
                    <Users className="w-4 h-4 mr-2" />
                    Manage Team
                  </Link>
                </Button>
              </CardContent>
            </Card>

            <Card className="bg-gradient-hero text-white border-0">
              <CardContent className="p-6">
                <div className="flex items-center mb-4">
                  <Clock className="w-8 h-8 mr-3" />
                  <div>
                    <h3 className="font-semibold">Today's Focus</h3>
                    <p className="text-white/90 text-sm">5 tasks due today</p>
                  </div>
                </div>
                <Button variant="secondary" size="sm" className="w-full">
                  View Tasks
                </Button>
              </CardContent>
            </Card>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Dashboard;