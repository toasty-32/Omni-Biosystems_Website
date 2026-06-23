import { useQuery } from '@tanstack/react-query'
import Navbar from '../components/ui/Navbar'
import { useAuth } from '../hooks/useAuth'
import { api } from '../lib/api'
import type { UserProfile } from '../types'

export default function ProfilePage() {
  const { user } = useAuth()
  const { data: profile } = useQuery<UserProfile>({
    queryKey: ['profile'],
    queryFn: () => api.get('/users/me').then((r) => r.data),
  })

  return (
    <div>
      <Navbar />
      <main style={styles.main}>
        <h2 style={styles.heading}>Profile</h2>
        <div style={styles.card}>
          <Row label="Email" value={user?.email ?? '—'} />
          <Row label="Display Name" value={profile?.displayName ?? '—'} />
          <Row label="Role" value={profile?.role ?? '—'} />
          <Row label="Organization" value={profile?.organization ?? '—'} />
          <Row label="Member Since" value={profile ? new Date(profile.createdAt).toLocaleDateString() : '—'} />
        </div>
      </main>
    </div>
  )
}

function Row({ label, value }: { label: string; value: string }) {
  return (
    <div style={styles.row}>
      <span style={styles.label}>{label}</span>
      <span style={styles.value}>{value}</span>
    </div>
  )
}

const styles: Record<string, React.CSSProperties> = {
  main: { maxWidth: '600px', margin: '0 auto', padding: '2rem 1.5rem' },
  heading: { fontSize: '1.5rem', fontWeight: 700, marginBottom: '1.5rem' },
  card: { background: 'var(--color-surface)', border: '1px solid var(--color-border)', borderRadius: 'var(--radius)', padding: '1.5rem', boxShadow: 'var(--shadow)' },
  row: { display: 'flex', justifyContent: 'space-between', padding: '0.75rem 0', borderBottom: '1px solid var(--color-border)' },
  label: { color: 'var(--color-muted)', fontSize: '0.875rem' },
  value: { fontWeight: 500, fontSize: '0.9rem' },
}
