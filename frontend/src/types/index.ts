export interface UserProfile {
  id: string
  email: string
  full_name: string | null
  role: 'admin' | 'researcher' | 'viewer'
  organization: string | null
  created_at: string
}

export interface Sample {
  id: string
  name: string
  type: string
  status: 'pending' | 'processing' | 'completed' | 'failed'
  collected_at: string
  processed_at: string | null
  owner_id: string
  metadata: Record<string, unknown>
}

export interface AnalysisResult {
  id: string
  sample_id: string
  result_type: string
  value: number
  unit: string
  reference_range: string | null
  flagged: boolean
  created_at: string
}

export interface DashboardStats {
  total_samples: number
  pending_samples: number
  completed_samples: number
  flagged_results: number
}
