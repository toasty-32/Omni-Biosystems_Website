import { useQuery } from '@tanstack/react-query'
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from 'recharts'
import Navbar from '../components/ui/Navbar'
import StatCard from '../components/dashboard/StatCard'
import { api } from '../lib/api'
import type { DashboardStats, Sample } from '../types'

export default function DashboardPage() {
  const { data: stats } = useQuery<DashboardStats>({
    queryKey: ['dashboard-stats'],
    queryFn: () => api.get('/dashboard/stats').then((r) => r.data),
  })

  const { data: samples } = useQuery<Sample[]>({
    queryKey: ['samples'],
    queryFn: () => api.get('/samples').then((r) => r.data),
  })

  const chartData = [
    { name: 'Pending', count: stats?.pending_samples ?? 0 },
    { name: 'Completed', count: stats?.completed_samples ?? 0 },
    { name: 'Flagged', count: stats?.flagged_results ?? 0 },
  ]

  return (
    <div>
      <Navbar />
      <main style={styles.main}>
        <h2 style={styles.heading}>Dashboard</h2>

        <div style={styles.statsGrid}>
          <StatCard label="Total Samples" value={stats?.total_samples ?? '—'} />
          <StatCard label="Pending" value={stats?.pending_samples ?? '—'} color="#f59e0b" />
          <StatCard label="Completed" value={stats?.completed_samples ?? '—'} color="var(--color-success)" />
          <StatCard label="Flagged Results" value={stats?.flagged_results ?? '—'} color="var(--color-error)" />
        </div>

        <div style={styles.section}>
          <h3 style={styles.sectionTitle}>Sample Status Overview</h3>
          <div style={styles.chart}>
            <ResponsiveContainer width="100%" height={260}>
              <BarChart data={chartData}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="name" />
                <YAxis allowDecimals={false} />
                <Tooltip />
                <Bar dataKey="count" fill="var(--color-primary)" radius={[4, 4, 0, 0]} />
              </BarChart>
            </ResponsiveContainer>
          </div>
        </div>

        <div style={styles.section}>
          <h3 style={styles.sectionTitle}>Recent Samples</h3>
          <table style={styles.table}>
            <thead>
              <tr>
                {['Name', 'Type', 'Status', 'Collected'].map((h) => (
                  <th key={h} style={styles.th}>{h}</th>
                ))}
              </tr>
            </thead>
            <tbody>
              {(samples ?? []).slice(0, 10).map((s) => (
                <tr key={s.id}>
                  <td style={styles.td}>{s.name}</td>
                  <td style={styles.td}>{s.type}</td>
                  <td style={styles.td}>
                    <span style={{ ...styles.badge, background: statusColor(s.status) }}>
                      {s.status}
                    </span>
                  </td>
                  <td style={styles.td}>{new Date(s.collected_at).toLocaleDateString()}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </main>
    </div>
  )
}

function statusColor(status: string) {
  const map: Record<string, string> = {
    pending: '#f59e0b',
    processing: '#3b82f6',
    completed: '#10b981',
    failed: '#ef4444',
  }
  return map[status] ?? '#6b7280'
}

const styles: Record<string, React.CSSProperties> = {
  main: { maxWidth: '1100px', margin: '0 auto', padding: '2rem 1.5rem' },
  heading: { fontSize: '1.5rem', fontWeight: 700, marginBottom: '1.5rem' },
  statsGrid: { display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', gap: '1rem', marginBottom: '2rem' },
  section: { background: 'var(--color-surface)', border: '1px solid var(--color-border)', borderRadius: 'var(--radius)', padding: '1.5rem', marginBottom: '1.5rem' },
  sectionTitle: { fontSize: '1rem', fontWeight: 600, marginBottom: '1rem' },
  chart: { width: '100%' },
  table: { width: '100%', borderCollapse: 'collapse' },
  th: { textAlign: 'left', padding: '0.625rem 0.75rem', fontSize: '0.8rem', textTransform: 'uppercase', color: 'var(--color-muted)', borderBottom: '2px solid var(--color-border)' },
  td: { padding: '0.75rem', fontSize: '0.9rem', borderBottom: '1px solid var(--color-border)' },
  badge: { padding: '0.2rem 0.6rem', borderRadius: '999px', color: '#fff', fontSize: '0.75rem', fontWeight: 600 },
}
