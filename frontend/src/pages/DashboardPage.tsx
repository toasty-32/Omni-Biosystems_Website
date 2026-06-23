import { useState } from 'react'
import { useQuery } from '@tanstack/react-query'
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from 'recharts'
import Navbar from '../components/ui/Navbar'
import StatCard from '../components/dashboard/StatCard'
import SampleForm from '../components/dashboard/SampleForm'
import Modal from '../components/ui/Modal'
import LoadingSpinner from '../components/ui/LoadingSpinner'
import ErrorBanner from '../components/ui/ErrorBanner'
import { api } from '../lib/api'
import type { DashboardStats, Sample } from '../types'

export default function DashboardPage() {
  const [showNewSample, setShowNewSample] = useState(false)

  const { data: stats, isLoading: statsLoading, isError: statsError, refetch: refetchStats } =
    useQuery<DashboardStats>({
      queryKey: ['dashboard-stats'],
      queryFn: () => api.get('/dashboard/stats').then((r) => r.data),
    })

  const { data: samples, isLoading: samplesLoading, isError: samplesError, refetch: refetchSamples } =
    useQuery<Sample[]>({
      queryKey: ['samples'],
      queryFn: () => api.get('/samples').then((r) => r.data),
    })

  const chartData = [
    { name: 'Pending', count: stats?.pendingSamples ?? 0 },
    { name: 'Completed', count: stats?.completedSamples ?? 0 },
    { name: 'Flagged', count: stats?.flaggedResults ?? 0 },
  ]

  return (
    <div>
      <Navbar />
      <main style={styles.main}>
        <div style={styles.pageHeader}>
          <h2 style={styles.heading}>Dashboard</h2>
          <button onClick={() => setShowNewSample(true)} style={styles.primaryBtn}>+ New Sample</button>
        </div>

        {statsError && <ErrorBanner message="Failed to load stats." onRetry={() => refetchStats()} />}

        {statsLoading ? <LoadingSpinner message="Loading stats…" /> : (
          <div style={styles.statsGrid}>
            <StatCard label="Total Samples" value={stats?.totalSamples ?? 0} />
            <StatCard label="Pending" value={stats?.pendingSamples ?? 0} color="#f59e0b" />
            <StatCard label="Completed" value={stats?.completedSamples ?? 0} color="var(--color-success)" />
            <StatCard label="Flagged Results" value={stats?.flaggedResults ?? 0} color="var(--color-error)" />
          </div>
        )}

        <div style={styles.section}>
          <h3 style={styles.sectionTitle}>Sample Status Overview</h3>
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

        <div style={styles.section}>
          <h3 style={styles.sectionTitle}>Recent Samples</h3>
          {samplesError && <ErrorBanner message="Failed to load samples." onRetry={() => refetchSamples()} />}
          {samplesLoading ? <LoadingSpinner /> : !samples?.length ? (
            <p style={styles.empty}>No samples yet. Create your first one above.</p>
          ) : (
            <table style={styles.table}>
              <thead>
                <tr>{['Name', 'Type', 'Status', 'Collected'].map((h) => <th key={h} style={styles.th}>{h}</th>)}</tr>
              </thead>
              <tbody>
                {samples.slice(0, 10).map((s) => (
                  <tr key={s.id}>
                    <td style={styles.td}>{s.name}</td>
                    <td style={styles.td}>{s.type}</td>
                    <td style={styles.td}>
                      <span style={{ ...styles.badge, background: statusColor(s.status) }}>{s.status}</span>
                    </td>
                    <td style={styles.td}>{new Date(s.collectedAt).toLocaleDateString()}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          )}
        </div>
      </main>

      {showNewSample && (
        <Modal title="New Sample" onClose={() => setShowNewSample(false)}>
          <SampleForm onSuccess={() => setShowNewSample(false)} />
        </Modal>
      )}
    </div>
  )
}

function statusColor(s: string) {
  return ({ pending: '#f59e0b', processing: '#3b82f6', completed: '#10b981', failed: '#ef4444' } as Record<string, string>)[s] ?? '#6b7280'
}

const styles: Record<string, React.CSSProperties> = {
  main: { maxWidth: '1100px', margin: '0 auto', padding: '2rem 1.5rem' },
  pageHeader: { display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: '1.5rem' },
  heading: { fontSize: '1.5rem', fontWeight: 700 },
  primaryBtn: { padding: '0.5rem 1.25rem', background: 'var(--color-primary)', color: '#fff', border: 'none', borderRadius: 'var(--radius)', fontSize: '0.9rem', fontWeight: 600, cursor: 'pointer' },
  statsGrid: { display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', gap: '1rem', marginBottom: '2rem' },
  section: { background: 'var(--color-surface)', border: '1px solid var(--color-border)', borderRadius: 'var(--radius)', padding: '1.5rem', marginBottom: '1.5rem' },
  sectionTitle: { fontSize: '1rem', fontWeight: 600, marginBottom: '1rem' },
  table: { width: '100%', borderCollapse: 'collapse' },
  th: { textAlign: 'left', padding: '0.625rem 0.75rem', fontSize: '0.8rem', textTransform: 'uppercase', color: 'var(--color-muted)', borderBottom: '2px solid var(--color-border)' },
  td: { padding: '0.75rem', fontSize: '0.9rem', borderBottom: '1px solid var(--color-border)' },
  badge: { padding: '0.2rem 0.6rem', borderRadius: '999px', color: '#fff', fontSize: '0.75rem', fontWeight: 600 },
  empty: { color: 'var(--color-muted)', fontSize: '0.9rem', textAlign: 'center', padding: '2rem 0' },
}
