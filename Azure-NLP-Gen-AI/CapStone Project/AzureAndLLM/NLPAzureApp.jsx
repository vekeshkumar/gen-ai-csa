import React, { useState, useCallback } from 'react';
import { Button } from "@/components/ui/button"
import { Textarea } from "@/components/ui/textarea"
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { Alert, AlertDescription, AlertTitle } from "@/components/ui/alert"
import { AlertCircle } from "lucide-react"
import { cn } from "@/lib/utils"

// Define the API base URL.  Make sure this matches your Flask backend.
const API_BASE_URL = 'http://localhost:5000'; // Or your deployed URL

const NLPAzureApp = () => {
    const [sentimentText, setSentimentText] = useState('');
    const [sentimentResult, setSentimentResult] = useState<{ sentiment: string; confidence_scores: any; error?: string } | null>(null);
    const [sentimentLoading, setSentimentLoading] = useState(false);

    const [summaryText, setSummaryText] = useState('');
    const [summaryResult, setSummaryResult] = useState<{ summary: string; error?: string } | null>(null);
    const [summaryLoading, setSummaryLoading] = useState(false);
    const [error, setError] = useState<string | null>(null);


    const handleSentimentAnalysis = useCallback(async () => {
        setSentimentLoading(true);
        setSentimentResult(null); // Clear previous result
        setError(null);
        try {
            const response = await fetch(`${API_BASE_URL}/sentiment`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ text: sentimentText }),
            });

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            const result = await response.json();
            if (result.error) {
                setError(result.error);
                setSentimentResult(null);
            }
            else {
                setSentimentResult(result);
            }

        } catch (err: any) {
            setError(err.message || 'An error occurred during sentiment analysis.');
            setSentimentResult(null);
        } finally {
            setSentimentLoading(false);
        }
    }, [sentimentText]);

    const handleSummarization = useCallback(async () => {
        setSummaryLoading(true);
        setSummaryResult(null); // Clear previous result
        setError(null);
        try {
            const response = await fetch(`${API_BASE_URL}/summary`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ text: summaryText }),
            });

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            const result = await response.json();
             if (result.error) {
                setError(result.error);
                setSummaryResult(null);
            }
            else {
                setSummaryResult(result);
            }
        } catch (err: any) {
            setError(err.message || 'An error occurred during summarization.');
            setSummaryResult(null);
        } finally {
            setSummaryLoading(false);
        }
    }, [summaryText]);

    return (
        <div className="min-h-screen bg-gradient-to-br from-gray-900 via-purple-900 to-black p-4 sm:p-8">
            <div className="max-w-4xl mx-auto space-y-8">
                <h1 className="text-3xl sm:text-4xl md:text-5xl font-bold text-center text-transparent bg-clip-text bg-gradient-to-r from-blue-400 to-purple-400">
                    Cloud-Based NLP Services
                </h1>

                {error && (
                    <Alert variant="destructive">
                        <AlertCircle className="h-4 w-4" />
                        <AlertTitle>Error</AlertTitle>
                        <AlertDescription>{error}</AlertDescription>
                    </Alert>
                )}

                <Card className="bg-white/5 backdrop-blur-md border border-white/10 shadow-lg">
                    <CardHeader>
                        <CardTitle className="text-2xl font-semibold text-white">Sentiment Analysis</CardTitle>
                        <CardDescription className="text-gray-300">Analyze the sentiment of customer reviews.</CardDescription>
                    </CardHeader>
                    <CardContent className="space-y-4">
                        <Textarea
                            placeholder="Enter text to analyze..."
                            value={sentimentText}
                            onChange={(e) => setSentimentText(e.target.value)}
                            className="bg-black/20 text-white border-purple-500/30 placeholder:text-gray-400 min-h-[120px]"
                        />
                        <Button
                            onClick={handleSentimentAnalysis}
                            disabled={sentimentLoading}
                            className={cn(
                                "w-full bg-gradient-to-r from-purple-500 to-blue-500 text-white",
                                "hover:from-purple-600 hover:to-blue-600",
                                "disabled:opacity-50 disabled:cursor-not-allowed",
                                "transition-all duration-300 shadow-lg hover:shadow-purple-500/50"
                            )}
                        >
                            {sentimentLoading ? 'Analyzing...' : 'Analyze Sentiment'}
                        </Button>
                        {sentimentResult && (
                            <div className="mt-4 p-4 rounded-lg bg-black/20 border border-white/10">
                                <h3 className="text-lg font-semibold text-purple-300">Result:</h3>
                                <p className="text-white">Sentiment: <span className="font-medium">{sentimentResult.sentiment}</span></p>
                                <div className="mt-2">
                                    <p className="text-gray-300">Confidence Scores:</p>
                                    <ul className="list-disc list-inside text-white">
                                        <li>Positive: {sentimentResult.confidence_scores.positive.toFixed(2)}</li>
                                        <li>Negative: {sentimentResult.confidence_scores.negative.toFixed(2)}</li>
                                        <li>Neutral: {sentimentResult.confidence_scores.neutral.toFixed(2)}</li>
                                    </ul>
                                </div>
                            </div>
                        )}
                    </CardContent>
                </Card>

                <Card className="bg-white/5 backdrop-blur-md border border-white/10 shadow-lg">
                    <CardHeader>
                        <CardTitle className="text-2xl font-semibold text-white">Document Summarization</CardTitle>
                        <CardDescription className="text-gray-300">Summarize academic papers or articles.</CardDescription>
                    </CardHeader>
                    <CardContent className="space-y-4">
                        <Textarea
                            placeholder="Enter text to summarize..."
                            value={summaryText}
                            onChange={(e) => setSummaryText(e.target.value)}
                            className="bg-black/20 text-white border-purple-500/30 placeholder:text-gray-400 min-h-[120px]"
                        />
                        <Button
                            onClick={handleSummarization}
                            disabled={summaryLoading}
                            className={cn(
                                "w-full bg-gradient-to-r from-purple-500 to-blue-500 text-white",
                                "hover:from-purple-600 hover:to-blue-600",
                                "disabled:opacity-50 disabled:cursor-not-allowed",
                                "transition-all duration-300 shadow-lg hover:shadow-purple-500/50"
                            )}
                        >
                            {summaryLoading ? 'Summarizing...' : 'Summarize'}
                        </Button>
                        {summaryResult && (
                            <div className="mt-4 p-4 rounded-lg bg-black/20 border border-white/10">
                                <h3 className="text-lg font-semibold text-purple-300">Summary:</h3>
                                <p className="text-white">{summaryResult.summary}</p>
                            </div>
                        )}
                    </CardContent>
                </Card>
            </div>
        </div>
    );
};

export default NLPAzureApp;